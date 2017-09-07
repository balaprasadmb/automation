#! /usr/bin/env ruby
require File.expand_path(File.join(File.dirname(__FILE__), '../config/environment.rb'))

CurrencyRate.seed

puts "   Organization Defaults"
Organization.seed_default_values

# Organization Defaults
puts "   Inventory Supplier Seat Defaults"
require 'inventory_supplier_seat.rb'
InventorySupplierSeat.seed_default_values

# System Seats Defaults
require 'system_seat.rb'
puts "   System Seat Defaults"
#SystemSeat.seed_default_values

require 'user.rb'

require 'declarative_authorization/maintenance.rb'

unless User.find_by_email('rwws@dataxu.com')
  Authorization::Maintenance.without_access_control do
    puts "Creating RWWS Callback User: 'rwws@dataxu.com'."

    rwws_agency_group = AgencyGroup.find_by_uid("0GUXmLlKVD")
    unless rwws_agency_group
      puts "Creating Org and Agency Group for RWWS Callback User"
      currency = Currency.where(iso_code: 'USD').first
      org = Organization.create! :currency => currency

      rwws_agency_group = AgencyGroup.create! :name            => "Machine Agency Group",
                                              :organization_id => org.id,
                                              :uid             => "UID that wont be repeated",
                                              :dataxu          => true
    end

    Authorization::Maintenance.without_access_control do
      u = User.new :email => 'rwws@dataxu.com',
                   :password => 'd940fe508b614c41a51f00ae02aab22b',
                   :password_confirmation => 'd940fe508b614c41a51f00ae02aab22b',
                   :organization => rwws_agency_group,
                   :active => Rails.env.test? || Rails.env.development?
      u.save(:validate => false)
    end
  end
else
  puts "RWWS Callback User: 'rwws@dataxu.com' already exists."
end

unless User.find_by_email('dx_admin@dataxu.com')
  Authorization::Maintenance.without_access_control do
    p "creating dx_admin:"

    p "creating org..."
    currency = Currency.where(iso_code: 'USD').first
    org = Organization.create! :currency => currency

    p "done."

    p "creating agency group..."
    agency_group = AgencyGroup.create! :name            => "Seed Agency Group",
                                       :organization_id => org.id,
                                       :uid             => "UID that wont be repeated"
    p "done."

    dx_admin_pword = 'P@22w0rd'

    p "creating user..."
    user = User.create! :email                 => 'dx_admin@dataxu.com',
                        :password              => dx_admin_pword,
                        :password_confirmation => dx_admin_pword,
                        :organization          => agency_group,
                        :active => Rails.env.test? || Rails.env.development?
    p "done."

    p "creating auth role..."
    UserAuthRole.create! :user      => user,
                         :auth_role => AuthRole.system_organization_administrator,
                         :scope     => Organization.defaults
    p "done."

    puts "Created default user. email: 'dx_admin@dataxu.com' pwd: #{dx_admin_pword}"
  end
else
  puts 'You \'dx_admin@dataxu.com\' user is already created.'
end

unless AgencyGroup.exists?(name: 'DataXu Managed Services')
  p "creating org..."
  currency = Currency.where(iso_code: 'USD').first
  org = Organization.create! :currency => currency

  p "done."

  p "creating agency group..."
  agency_group = AgencyGroup.where(name: 'DataXu Managed Services', organization_id: org.id, uid: 'UID that wont be repeated').first_or_create
  p "creating agency"
  Agency.where(name: 'dataxu agency', agency_group_id: agency_group.id, organization_id: agency_group.organization.id).first_or_create
  Agency.where(name: 'dataxu test agency', agency_group_id: agency_group.id, organization_id: agency_group.organization.id).first_or_create
  p "done."
else
  puts "Agency group 'DataXu Managed Services' is already present.."
end

unless AgencyGroup.exists?(name: 'dataxu')
  p "creating org..."
  currency = Currency.where(iso_code: 'USD').first
  org = Organization.create! :currency => currency

  p "done."

  p "creating agency group..."
  agency_group = AgencyGroup.where(name: 'dataxu', organization_id: org.id, uid: 'UID that wont be repeated').first_or_create
  p "creating agency"
  Agency.where(name: 'seed agency', agency_group_id: agency_group.id, organization_id: agency_group.organization.id).first_or_create
  p "done."
else
  puts "Agency group 'dataxu' is already present.."
end

puts "Create Users from Registration Screen with Proper Role as desired"
puts "Created users will be assigned to selected Agency Group, Agency or Advertiser"

puts '...done.'
