# 
reference : https://medium.com/coinmonks/coding-a-smart-world-series-330fe8b27db9

Issues resolved : 

`now` has been deprecated replaced with `block.timestamp`

`.send` and `.transfer` functions are now supported only for type payable. `payable(msg.sender).send(amount)` resolved

https://stackoverflow.com/questions/67341914/error-send-and-transfer-are-only-available-for-objects-of-type-address-payable

https://github.com/ethereum/solidity/issues/4020