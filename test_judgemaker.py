from judge_maker import make_judge
# No1
def test_makejudge():
    result = make_judge("E",[9,100,100,100,100,100,100,100,100,100])
    assert result == 3
#No2
def test_makejudge2():
    result = make_judge("E",[29,29,29,100,100,100,100,100,100,100])
    assert result == 2
#No3
def test_makejudge3():
    result = make_judge("A",[100,100,100,100,100,100,100,100,100,100])
    assert result == 1
#No4
def test_makejudge4():
    result = make_judge("D",[100,100,100,100,100,100,100,100,100,100])
    assert result == 2
#No5
def test_makejudge5():
    result = make_judge("E",[100,100,100,100,100,100,100,100,100,100])
    assert result == 3