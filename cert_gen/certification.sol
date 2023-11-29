// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Certification {
    constructor() {}

    struct Certificate {
        string candidate_name;
        // string org_name;
        string course_name;
        string issue_date;
    }

    mapping(bytes32 => Certificate) public certificates;

    event certificateGenerated(bytes32 _certificateId);

    function stringToBytes32(string memory source) private pure returns (bytes32 result) {
        bytes memory tempEmptyStringTest = bytes(source);
        if (tempEmptyStringTest.length == 0) {
            return 0x0;
        }
        assembly {
                result := mload(add(source, 32))
        }
    }

    function generateCertificate(
        string memory _id,
        string memory _candidate_name, 
        string memory _course_name, 
        string memory _issue_date) public {
        bytes32 byte_id = stringToBytes32(_id);
        // require(certificates[byte_id].issue_date == 0, "Certificate with given id already exists");
        certificates[byte_id] = Certificate(_candidate_name, _course_name, _issue_date);
        emit certificateGenerated(byte_id);
    }

    function getData(string memory _id) public view returns(string memory, string memory,  string memory) {
        bytes32 byte_id = stringToBytes32(_id);
        Certificate memory temp = certificates[byte_id];
        // require(temp.issue_date != 0, "No data exists");
        return (temp.candidate_name,  temp.course_name, temp.issue_date);
    }
}