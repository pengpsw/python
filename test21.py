# coding:utf-8
import hmac

secret_key1 = b'This is my secret key'
message1 = b'Hello world'
hex_res1 = hmac.new(secret_key1, message1, digestmod="MD5").hexdigest()
print(hex_res1)  # b8908a20bd70f465330b434e18441d3b

secret_key2 = b'This is my secret key'
message2 = b'Hello world'
hex_res2 = hmac.new(secret_key2, message2, digestmod="MD5").hexdigest()
print(hex_res2)  # b8908a20bd70f465330b434e18441d3b

compare_res = hmac.compare_digest(hex_res1, hex_res2)  # 比较两个密文是否相同
print(compare_res)  # True

secret_key3 = b'This is my secret key'
message3 = b'Hello world!'
hex_res3 = hmac.new(secret_key3, message3, digestmod="MD5").hexdigest()
print(hex_res3)  # a314490e13ff3d1dfa9cd18db8c4c3e8

compare_res = hmac.compare_digest(hex_res1, hex_res3)  # 比较两个密文是否相同
print(compare_res)  # False

hmac_hex = hmac.new(secret_key3, message3, digestmod='md5').hexdigest()
print(hmac_hex)  # a314490e13ff3d1dfa9cd18db8c4c3e8
print(hmac.new(secret_key3, message3, 'md5').digest())  # b'\xa3\x14I\x0e\x13\xff=\x1d\xfa\x9c\xd1\x8d\xb8\xc4\xc3\xe8'
print(len(hmac.new(secret_key3, message3, 'md5').digest()))  # 16

content = "hello world"
content_bytes = content.encode("utf-8")
content_bytes_upper = content_bytes.upper()  # 今天才知道,还可以对bytes进行upper
print(content_bytes_upper.decode("utf-8"))  # HELLO WORLD