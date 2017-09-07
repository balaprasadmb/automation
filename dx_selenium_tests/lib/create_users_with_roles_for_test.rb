require File.expand_path(File.join(File.dirname(__FILE__), '../config/environment.rb'))

# provide User Role As Input

def create_user_with_role_and_email(auth_role_name, email, new_features=[], organization_type = nil, organization = nil)
  Authorization.ignore_access_control(true)
  
  User.where(email: email).destroy_all
  auth_role_names = auth_role_name.split(',').map(&:strip).map {|role| role.strip.gsub(/\W/, '_').snakecase.to_sym}

  auth_role_names.each do |role|
    raise "AuthRole #{role} not in #{AuthRole::KEYS.join(',')}" unless AuthRole::KEYS.include?(role)
  end

  auth_roles = auth_role_names.map {|role| AuthRole.send(role.to_sym)}

  organization ||= organization_type.try(:classify).try(:constantize).try(:make)

  organization ||=
    if [
      :system_organization_administrator,
      :system_support_user,
      :system_administrator
    ].include?(auth_role_names.first.to_sym)
      Organization.defaults
    elsif [
      :organization_administrator,
      :user_administrator
    ].include?(auth_role_names.first.to_sym)
      AgencyGroup.where(name: ['DataXu Managed Services', 'dataxu']).first 
    else
      @agency_group ||= AgencyGroup.where(name: ['DataXu Managed Services', 'dataxu']).first
    end

  user = User.create(organization: organization.is_a?(Organization) ? AgencyGroup.where(name: ['DataXu Managed Services', 'dataxu']).first : organization,
                     password: 'P@22w0rd',
                     active: true,
                     email: email
  )

  auth_roles.each do |role|
    UserAuthRole.create!(:user => user, :auth_role => role, :scope => organization)
  end

  #Specify Product Feature as per requirement
  product_features = if auth_roles.include?(AuthRole.campaign_manager)
    ["guaranteed-inventory", "custom-inventory", "deal-inventory", "forecasting", 
     "geohashing", "mobile-rich-media", "inheritable-add-on-costs", "custom-add-on-cost"] + new_features
  else
    ['inheritable-add-on-costs', 'guaranteed-inventory', 'omnichannel'] + new_features
  end

  UserAuthRole.create!:user => user, :auth_role => AuthRole.system_organization_administrator, :scope => organization if auth_roles.include?(AuthRole.system_support_user)
  ProductFeature.where(key: product_features).map {|pr| pr.make_available_to_users( ProductFeatureUser.where(product_feature_id: pr.id).map(&:user_id) + [user] ) }
  Authorization.ignore_access_control(false)
end

['dx_agency', 'dx_agency_group', 'dx_organization_admin', 'dx_advertiser', 'dx_sys_admin_one_view'].each do |role|
  create_user_with_role_and_email('System Organization Administrator',  role + '@dataxu.com')
end

# Campaign manager
create_user_with_role_and_email('Campaign Manager, Inventory Manager', 'dx_campaign@dataxu.com', ['activity-sharing', 'activity-third-party-server', 'segment-sharing',
                                'FBX', 'FBX-PPA', 'one-impression-per-page', 'omnichannel', 'device-targeting', 'omnichannel-viewability'])
# Inventory Manager
create_user_with_role_and_email('Inventory Manager', 'dx_inventory@dataxu.com')
# Campaign Manager With One View
create_user_with_role_and_email('Campaign Manager', 'dx_campaign_one_view@dataxu.com')
#Campaign manager-Non dataxu user
create_user_with_role_and_email('Campaign Manager', 'dx_non@domain.com')
