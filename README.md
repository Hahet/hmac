### HMAC是密钥相关的哈希运算消息认证码（Hash-based Message Authentication Code）的缩写

### 实现步骤

### 处理 key

key 的长度如果小于 block_size 则在 key 后面补 0

key 的长度如果大于 block_size 则 key = sha1(key).digest()， 如果计算的key长度小于block_size, 需要补 0

### outer_pad inner_pad

outer_pad 是用 0x5c 这个数字 xor 处理 key 的每个字节
inner_pad 是用 0x36 这个数字 xor 处理 key 的每个字节

### 得到 hmac

hmac = sha1(outer_pad + sha1(inner_pad + message))
