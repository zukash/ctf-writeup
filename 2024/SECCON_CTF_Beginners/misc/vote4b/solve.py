# README.md を読む

"""
攻撃者: 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80
被害者: 0x59c6995e998f97a5a0044966f0945389dc9e86dae88c7a8412f4603b6b78690d

$ forge create --rpc-url localhost:8545 --private-key 0x59c6995e998f97a5a0044966f0945389dc9e86dae88c7a8412f4603b6b78690d src/Setup.sol:Setup
[⠒] Compiling...
[⠢] Compiling 14 files with Solc 0.8.26
[⠆] Installing Solc version 0.8.26
[⠒] Successfully installed Solc 0.8.26
[⠘] Solc 0.8.26 finished in 4.31s
Compiler run successful!
Deployer: 0x70997970C51812dc3A010C7d01b50e0d17dc79C8
Deployed to: 0x8464135c8F25Da09e49BC8782676a84730C318bC
Transaction hash: 0x2572127b5a64b969aaee58ad4d76d637062476515b5891c85523fe8a78aad92d


$ forge script --rpc-url localhost:8545 --private-key 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80 --broadcast script/Exploit.s.sol:Exploit

$ forge script --rpc-url http://vote4b.beginners.seccon.games:64505/7889389cabab/rpc --private-key 0x4adc00b4e8ce6c807343a0a7c5f29f1c4ec80f21cf34a294f2bd1c65feed3520 --broadcast script/Exploit.s.sol:Exploit

$ forge create --rpc-url http://vote4b.beginners.seccon.games:64505/7889389cabab/rpc --private-key 0x4adc00b4e8ce6c807343a0a7c5f29f1c4ec80f21cf34a294f2bd1c65feed3520 src/Setup.sol:Setup





"""