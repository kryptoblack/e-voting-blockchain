// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.5.0;

contract VotingMachine {
    uint256 public totalVotes;
    uint256 public candidateCount;
    uint256 public winner;

    struct Candidate {
        string organization;
        string candidateName;
        string partyName;
        uint256 voteCount;
        bool isWinner;
    }

    mapping(uint256 => Candidate) public candidates;

    event CandidateAdded(
        string candidateName,
        string partyName,
        uint256 voteCount,
        uint256 candidateNo,
        string organization
    );

    event VoteCasted(
        uint256 candidateNo,
        string candidateName,
        string partyName
    );

    constructor() {
        totalVotes = 0;
        candidateCount = 0;
        addCandidate(
            "Ritesh",
            "BJP",
            "0x201196A878eFD8357953238a10C0F5d99fCf932e"
        );
    }

    function addCandidate(
        string memory _cName,
        string memory _pName,
        string memory _oName
    ) public {
        uint256 _vcount = 0;
        candidates[candidateCount++] = Candidate(
            _oName,
            _cName,
            _pName,
            _vcount,
            false
        );

        // emit event
        emit CandidateAdded(
            _cName,
            _pName,
            candidateCount - 1,
            _vcount,
            _oName
        );
    }

    function casteVote(
        uint256 _cId,
        string memory _candName,
        string memory _partName
    ) public {
        totalVotes++;
        candidates[_cId].voteCount++;

        emit VoteCasted(_cId, _candName, _partName);
    }

    function compareStrings(string memory a, string memory b)
        internal
        pure
        returns (bool)
    {
        return (keccak256(abi.encodePacked((a))) ==
            keccak256(abi.encodePacked((b))));
    }

    function getWinner(string memory _oName) public returns (uint256) {
        uint256 max = 0;

        for (uint256 i = 0; i < candidateCount; i++) {
            if (
                compareStrings(_oName, candidates[i].organization) &&
                candidates[i].voteCount > max
            ) {
                max = candidates[i].voteCount;
                winner = i;
            }
        }

        return winner;
    }
}
