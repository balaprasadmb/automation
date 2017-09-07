import sys
import os
import paramiko
from paramiko.ssh_exception import AuthenticationException, SSHException, BadHostKeyException
from configs.dx_constant import DXConstant

class SkytapSetup(object):

    def __init__(self, host):
        try:
            self.conn = paramiko.SSHClient()
            self.conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.conn.connect(host, username='dataxu', password='dataxu', look_for_keys=False, allow_agent=False)
        except AuthenticationException:
            print("Authentication failed, please verify your credentials: %s")
        except SSHException as sshException:
            print("Unable to establish SSH connection: %s" % sshException)
        except BadHostKeyException as badHostKeyException:
            print("Unable to verify server's host key: %s" % badHostKeyException)
        except Exception as e:
            print("Operation error: %s" % e)

    def ssh_to_skytap(self, command):

        try:
            stdin, stdout, stderr = self.conn.exec_command(command)
            print "output:- %s" % str(stdout.read())
        except AuthenticationException:
            print("Authentication failed, please verify your credentials: %s")
        except SSHException as sshException:
            print("Unable to establish SSH connection: %s" % sshException)
        except BadHostKeyException as badHostKeyException:
            print("Unable to verify server's host key: %s" % badHostKeyException)
        except Exception as e:
            print("Operation error: %s" % e)
        finally:
            self.conn.close()

    def copy_to_skytap(self, localpath, remotepath):
        try:
            sftp = self.conn.open_sftp()
            sftp.put(localpath, remotepath)
        except Exception as e:
            print("Operation error: %s" % e)
        finally:
            sftp.close()
            self.conn.close()

if __name__ == "__main__":
    #Seed database
    SkytapSetup(sys.argv[1]).copy_to_skytap(os.path.dirname(__file__) + '/seeds.rb', '/opt/dataxu/webapps/ui/current/db/seeds.rb')
    SkytapSetup(sys.argv[1]).ssh_to_skytap('cd /opt/dataxu/webapps/ui/current; /opt/dataxu/dxuser/.bash_profile; ./bin/server_setup.sh')
    SkytapSetup(sys.argv[1]).ssh_to_skytap('cd /opt/dataxu/webapps/ui/current; source ~/.bash_profile; DB_MIGRATE=true bundle exec rake db:migrate db:seed')
    SkytapSetup(sys.argv[1]).ssh_to_skytap('echo "NEW_USER_BYPASS_EMAIL_VERIFY=true\nNEW_USER_BYPASS_EMAIL_DEFAULT_PASSWORD=%s" >> /opt/dataxu/shared/.env.staging'% DXConstant().password.decode("base64", 'strict'))
    SkytapSetup(sys.argv[1]).ssh_to_skytap('touch /opt/dataxu/shared/tmp/restart.txt')
