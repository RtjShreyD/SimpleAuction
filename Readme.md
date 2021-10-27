# 
reference : https://medium.com/coinmonks/coding-a-smart-world-series-330fe8b27db9

Issues resolved : 

`now` has been deprecated replaced with `block.timestamp`

`.send` and `.transfer` functions are now supported only for type payable. `payable(msg.sender).send(amount)` resolved

https://stackoverflow.com/questions/67341914/error-send-and-transfer-are-only-available-for-objects-of-type-address-payable

https://github.com/ethereum/solidity/issues/4020

#
How does truffle know which account to charge gas fee while deploying ?

https://ethereum.stackexchange.com/questions/58588/how-does-truffle-know-which-address-to-send-a-contract-being-migrated-and-which

# Todo

1. Implement the /bid and /highest-bid routes
2. Find a way to catch the sol emitted event in Python
3. Connect app with Metamask
4. Write tests
5. Deploy app to production