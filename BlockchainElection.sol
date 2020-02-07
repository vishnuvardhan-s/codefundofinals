pragma solidity 0.4.25;

contract BlockchainElection {

    enum StateType {SignUpState, VotingState, ResultState}

    StateType public State;

    struct Candidate {
        int CandidateId;
        string CandidateName;
        int VoteCount;
    }

    address public ElectionHead;
    address public Voter;
    address public ZoneRepresentative;
    int public CandidatesCount;
    string public Winner;
    string public CandidateName;
    int public CandidateId;
    string public Title;
    mapping(address => bool) public voters;
    mapping(int => Candidate) public candidates;

    constructor (string TitleT) public {
        Title = TitleT;
        CandidatesCount = -1;
        AddCandidate("");
        State = StateType.SignUpState;
    }

    function AllowVoting () public {
        State = StateType.VotingState;
    }

    function Vote (int CandidateId) public {

        require(!voters[msg.sender], "You have voted already!");

        voters[msg.sender] = true;
        
        candidates[CandidateId].VoteCount ++;

        State = StateType.VotingState;
    }

    function AddCandidate (string CandidateName) public {
        CandidatesCount ++;
        candidates[CandidatesCount] = Candidate(CandidatesCount, CandidateName, 0);
    }

    function CalculateResult () public {
        int maximum = 0;
        for (int i = 0;i <= CandidatesCount;i++){
            if (candidates[i].VoteCount > maximum){
                Winner = candidates[i].CandidateName;
                maximum = candidates[i].VoteCount;
            }
        }
        State = StateType.ResultState;
    }
}