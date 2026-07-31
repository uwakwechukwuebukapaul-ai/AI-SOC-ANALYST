from evidence_engine.ioc.extractor import ioc_extractor


sample = """

Suspicious login detected.

User connected from:

192.168.1.55


Email:

attacker@evil-login.xyz


Website:

https://evil-login.xyz/verify


File hash:

44d88612fea8a8f36de82e1278abb02f

"""


result = ioc_extractor.summary(sample)


print("=" * 50)

print("SENTINEL DNA IOC EXTRACTION")

print("=" * 50)


print(result)