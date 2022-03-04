Originally written to enumerate Azure cloud domains, although the domains and permutations arguments could be applied to any dns enumeration.

Based on MicroBurst from NetSPI - https://github.com/netspi/microburst Swiped the permutations.txt and the list of subdomains from there.

Wrote my own because the ps1 file was super slow in my Windows VM and it's quicker for me to write python than to understand powershell.

```
(.env) danny@Dannys-MBP subdomain_enum % python ./subdomain_enum.py -h
usage: subdomain_enum.py [-h] [--base BASE] [--permutations PERMUTATIONS] [--domains DOMAINS] [--outfile OUTFILE]

Enumerate Azure Cloud resources

optional arguments:
  -h, --help            show this help message and exit
  --base BASE           Base word
  --permutations PERMUTATIONS
                        File containing permutations
  --domains DOMAINS     File containing domains
  --outfile OUTFILE     Output file

  (.env) danny@Dannys-MBP subdomain_enum % python ./subdomain_enum.py --base test --outfile out.txt
Exists but no IP for apitest.onmicrosoft.com
Exists but no IP for azuretest.onmicrosoft.com
Exists but no IP for testazure.onmicrosoft.com
Exists but no IP for cheftest.onmicrosoft.com
Exists but no IP for clienttest.onmicrosoft.com
Exists but no IP for testclient.onmicrosoft.com
Exists but no IP for configtest.onmicrosoft.com
Exists but no IP for testconfig.onmicrosoft.com
<...snip...>
Exists but no IP for testsplunk.onmicrosoft.com
Exists but no IP for sshtest.onmicrosoft.com
Exists but no IP for stagingtest.onmicrosoft.com
Exists but no IP for storagetest.onmicrosoft.com
Exists but no IP for testtest.onmicrosoft.com
Exists but no IP for testtest.onmicrosoft.com
Exists but no IP for testtmp.onmicrosoft.com
Exists but no IP for westustest.onmicrosoft.com
Exists but no IP for testweb.onmicrosoft.com
Exists but no IP for imgtest.onmicrosoft.com
test.onmicrosoft.com exists
apitest.scm.azurewebsites.net exists
testapi.scm.azurewebsites.net exists
api-test.scm.azurewebsites.net exists
test-api.scm.azurewebsites.net exists
assetstest.scm.azurewebsites.net exists
azuretest.scm.azurewebsites.net exists
testazure.scm.azurewebsites.net exists
azure-test.scm.azurewebsites.net exists
test-azure.scm.azurewebsites.net exists
chef-test.scm.azurewebsites.net exists
clienttest.scm.azurewebsites.net exists
testclient.scm.azurewebsites.net exists
test-client.scm.azurewebsites.net exists
<...snip...>
  ```
