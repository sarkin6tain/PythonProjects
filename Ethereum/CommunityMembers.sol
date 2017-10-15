pragma solidity ^0.4.0;

contract CommunityMembers {

    address[] members;

    function isRegistered(address member) constant returns(bool registered){
        for(uint32 i = 0; i < members.length; i++){
            if(members[i] == member) {
                return true;
            }
        }
        return false;
    }

    function getMembers() constant returns(address[]) {
        return members;
    }

    function register() {
        if(!this.isRegistered(msg.sender)) {
            members.push(msg.sender);
        }
    }
}