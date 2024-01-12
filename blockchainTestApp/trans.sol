// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract trans{
    string public result;
    // function save(string memory _msg) public{
    //     result = _msg;
    // }
    function save(bytes memory binary_result) public {
        result = string(binary_result);
    }
}
