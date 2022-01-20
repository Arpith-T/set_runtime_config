import subprocess


def aciat001_oauth_token():
    login = subprocess.run(f'cf login -a https://api.cf.sap.hana.ondemand.com -o "CPI-Global-Canary_aciat001"  -s prov_eu10_aciat001 -u prism@global.corp.sap -p Prisminfra529#5')
    # print(login)

    oauth_token = subprocess.run("cf oauth-token", stdout=subprocess.PIPE)

    oauth_token_string = str(oauth_token.stdout)

    return oauth_token_string[2:-3]