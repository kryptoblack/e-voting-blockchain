abi = [
  {
    "inputs": [],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": False,
        "internalType": "string",
        "name": "candidateName",
        "type": "string"
      },
      {
        "indexed": False,
        "internalType": "string",
        "name": "partyName",
        "type": "string"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "voteCount",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "candidateNo",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "string",
        "name": "organization",
        "type": "string"
      }
    ],
    "name": "CandidateAdded",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "candidateNo",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "string",
        "name": "candidateName",
        "type": "string"
      },
      {
        "indexed": False,
        "internalType": "string",
        "name": "partyName",
        "type": "string"
      }
    ],
    "name": "VoteCasted",
    "type": "event"
  },
  {
    "inputs": [],
    "name": "candidateCount",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function",
    "constant": True
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "name": "candidates",
    "outputs": [
      {
        "internalType": "string",
        "name": "organization",
        "type": "string"
      },
      {
        "internalType": "string",
        "name": "candidateName",
        "type": "string"
      },
      {
        "internalType": "string",
        "name": "partyName",
        "type": "string"
      },
      {
        "internalType": "uint256",
        "name": "voteCount",
        "type": "uint256"
      },
      {
        "internalType": "bool",
        "name": "isWinner",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function",
    "constant": True
  },
  {
    "inputs": [],
    "name": "totalVotes",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function",
    "constant": True
  },
  {
    "inputs": [],
    "name": "winner",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function",
    "constant": True
  },
  {
    "inputs": [
      {
        "internalType": "string",
        "name": "_cName",
        "type": "string"
      },
      {
        "internalType": "string",
        "name": "_pName",
        "type": "string"
      },
      {
        "internalType": "string",
        "name": "_oName",
        "type": "string"
      }
    ],
    "name": "addCandidate",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_cId",
        "type": "uint256"
      },
      {
        "internalType": "string",
        "name": "_candName",
        "type": "string"
      },
      {
        "internalType": "string",
        "name": "_partName",
        "type": "string"
      }
    ],
    "name": "casteVote",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "string",
        "name": "_oName",
        "type": "string"
      }
    ],
    "name": "getWinner",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  }
]