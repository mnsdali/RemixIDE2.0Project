// Simple smart contract that stores and returns a string
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MyContract {
    string private myString;

    function set(string memory newString) public {
        myString = newString;
    }

    function get() public view returns (string memory) {
        return myString;
    }
}