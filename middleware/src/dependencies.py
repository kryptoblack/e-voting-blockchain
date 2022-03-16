from web3 import Web3

from src.abi import abi

# Blockchain connection
class Web3Client():
    __w3 = None
    __instance = None
    __contract_abi = abi
    __contract_address = '0xb1Fc2313612064EEeeb232815481BF6c8bb7c280'


    @classmethod
    def get_client(cls):
        if not cls.__instance:
            cls.__instance = Web3Client()
            if not cls.__w3:
                cls.__w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
        return cls.__instance


    def get_contract(self):
        return self.__w3.eth.contract(self.__contract_address, abi=self.__contract_abi)


    def get_accounts(self):
        return self.__w3.eth.accounts


    def get_candidate_count(self):
        return self.get_contract().functions.candidateCount().call()

    
    def get_candidate(self, candidate_no: int) -> list:
        return self.get_contract().functions.candidates(candidate_no).call()


    def add_candidate(self, name: str, party: str, frm: str) -> bool:
        # Send transaction
        tx_hash = self.get_contract().functions.addCandidate(name, party, frm).transact({ 'from': frm })
        
        # Mine receipt
        receipt = self.__w3.eth.wait_for_transaction_receipt(tx_hash)

        if receipt['status'] == 1:
            return True
        return False

    
    def caste_vote(self, candidate_no: int, name: str, party: str, frm: str) -> bool:
        # Send transaction
        tx_hash = self.get_contract().functions.casteVote(candidate_no, name, party).transact({ 'from': frm })
        
        # Mine receipt
        receipt = self.__w3.eth.wait_for_transaction_receipt(tx_hash)

        if receipt['status'] == 1:
            return True
        return False


    def get_winner(self, frm: str) -> list:
        # Send transaction
        # tx_hash = self.get_contract().functions.getWinner(frm).transact({ 'from': frm })

        # print(tx_hash)
        
        # # Mine receipt
        # receipt = self.__w3.eth.wait_for_transaction_receipt(tx_hash)

        # print(receipt)
        # if receipt['status'] == 1:
        #     return True
        # return False
        winner = list()
        max_votes = 0
        for i in range(self.get_candidate_count()):
            candidate = self.get_candidate(i)
            if candidate[0] == frm:
                print(candidate)
                if max_votes < candidate[3]:
                    candidate[4] = i
                    winner = [candidate]
                    max_votes = candidate[3]
                elif max_votes == candidate[3]:
                    candidate[4] = i
                    winner.append(candidate)

        return winner
        