var SimpleAuction = artifacts.require("SimpleAuction");

module.exports = function(deployer) {
    deployer.deploy(SimpleAuction, 3000, "0x9EAf14e7AF0c981e2976Bcc024c790f3eFf8e2cb");
};