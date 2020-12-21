import pytest

def get_vote_count(votes):
    upvotes = votes.get("upvotes")
    downvotes = votes.get("downvotes")
    
    resp = upvotes - downvotes
    return resp

def test_answer():
    assert(get_vote_count({"upvotes" : 2, "downvotes" : 33})) == -31
