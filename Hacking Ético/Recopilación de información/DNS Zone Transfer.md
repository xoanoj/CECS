
DNS Interrogation: The process of enumerating DNS records for a specific domain

Zone transfer: copying or transfering zone files from one DNS server to another. If misconfigured the functionality can be abused to copy the zone files from the primary dns to another DNS server.

A DNS Zone transfer can give a pentester a holistic view of an organizations network layout. Internal network addresses may also be found.

DNS enum can enumerate accesible records and do DNS bruteforcing, but this is active recon.

``` bash
dnsenum [domainname]
```

Dig can also be used:

``` bash
dig axfr [domainname]
```

Where axfr is the zonetransfer switch.

Fierce may also be used:

``` bash
fierce -dns [domainname]
```