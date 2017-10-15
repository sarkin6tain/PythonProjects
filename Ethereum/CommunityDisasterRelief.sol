pragma solidity ^0.4.0;

import "browser/CommunityMembers.sol";

contract CommunityDisasterRelief {

    event Error(string message);
    event Vote(uint32[] votes);

    mapping (uint32 => uint32) votes;
    mapping (address => uint32[]) usersPreviousVotes;
    mapping (uint32 => PromisedItem) promiseItems;

    struct PromisedItem {
        uint32 quantity;
        uint32 price;
        address seller;
    }

    CommunityMembers communityMembers;

    function CommunityDisasterRelief(address comunityMembersAddress) {
        communityMembers  = CommunityMembers(comunityMembersAddress);

        votes[0] = 0; //generators
        votes[1] = 0; //tents
        votes[2] = 0; //blankets
        votes[3] = 0; //water
        votes[4] = 0; //food
        votes[5] = 0; //clothes
        votes[6] = 0; //sandbags
        votes[7] = 0; //bloodbanks
        votes[8] = 0; //aidkits
        votes[9] = 0; //ps4 games;
    }

    function vote(uint32[] yourVotes){
        if(communityMembers.isRegistered(msg.sender)){
            uint32[] prevVotes = usersPreviousVotes[msg.sender];
            for(uint32 i = 0; i < prevVotes.length; i++) {
                votes[prevVotes[i]]--;
            }

            for(uint32 j = 0; j < yourVotes.length; j++) {
                votes[yourVotes[j]]++;
            }

            usersPreviousVotes[msg.sender] = yourVotes;
        }
        else
        {
            Error("Not AUthorized");
        }

    }

    function getVotes(uint32 voteIndex) constant returns(uint32) {
        return votes[voteIndex];
    }

    function sendFunds() payable {

    }

    function promiseItem(uint32 index, uint32 quantity, uint32 price){
        promiseItems[index] = PromisedItem(quantity, price, msg.sender);
    }

    function eventHappened() {
        uint32 index = 0;
        uint32 topVoted = 0;
        for(uint32 i; i < 10; i++){
             if(votes[i] > topVoted) {
                 topVoted = votes[i];
                 index = i;
             }
        }

        promiseItems[index].seller.send(promiseItems[index].price);
    }

    function getBalance() constant returns(uint) {
        return this.balance;
    }
}