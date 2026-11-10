"""MQR 5.4 / chat MQR 41: protocol discovery under a finite menu.

No claim that operator grammars are created ex nihilo.
All samples use repeatably prepared initial states; instrument artifact depends
on a session-dependent nuisance variable not included in the physical state.
"""
from itertools import product

STATES = tuple(product((0, 1), repeat=3))

def flip_x(s): return (1-s[0],s[1],s[2])
def flip_y(s): return (s[0],1-s[1],s[2])
def swap_xy(s): return (s[1],s[0],s[2])
def swap_xz(s): return (s[2],s[1],s[0])

# Operators (not world-generating proposals): concrete candidate protocols.
OPERATORS = {
    'flip_x': flip_x, 'flip_y': flip_y,
    'swap_xy': swap_xy, 'swap_xz': swap_xz,
}

def readout(name, state, session):
    if name == 'artifact':
        # A false sensor, returning a session-correlated tag, NOT a physical x readout.
        return state[1] if session == 'training' else state[2]
    return OPERATORS[name](state)[0]

def sig(state, chosen, session):
    return (state[0],) + tuple(readout(name,state,session) for name in chosen)

def partition(chosen, session):
    return len({sig(s,chosen,session) for s in STATES})

def stable(chosen):
    return all(sig(s,chosen,'training') == sig(s,chosen,'independent') for s in STATES)

def choose():
    menu = sorted([*OPERATORS,'artifact'])
    selected=[]
    transcript=[]
    # Audit every offered action before any greedy gain-based selection.
    # Otherwise a confounded candidate can escape inspection after valid actions saturate the partition.
    validated=[]
    for name in menu:
        if not stable([name]):
            transcript.append((name, partition([name],'training')-partition([],'training'), 'REJECT: session-unstable artifact'))
        else:
            validated.append(name)
    menu=validated
    while True:
        prior=partition(selected,'training')
        proposed=sorted(((partition([*selected,name],'training')-prior,name) for name in menu if name not in selected),reverse=True)
        accepted=None
        for gain,name in proposed:
            if gain <= 0: break
            if not stable([*selected,name]):
                transcript.append((name, gain, 'REJECT: session-unstable artifact'))
                continue
            accepted=(name,gain)
            break
        if accepted is None: break
        name,gain=accepted
        selected.append(name)
        transcript.append((name,gain,'ACCEPT'))
    return selected,transcript

def check():
    assert partition([], 'training') == 2
    assert partition(['flip_x','flip_y'], 'training') == 2
    assert partition(['swap_xy'], 'training') == 4
    assert partition(['swap_xz'], 'training') == 4
    assert partition(['swap_xy','swap_xz'], 'training') == 8
    assert partition(['artifact'], 'training') == 4
    assert partition(['artifact'], 'independent') == 4 # FALSE REASSURANCE BY COUNT ALONE
    assert not stable(['artifact'])
    assert stable(['swap_xy','swap_xz'])
    selected,transcript=choose()
    assert set(selected) == {'swap_xy','swap_xz'}
    assert any(t[0]=='artifact' and t[2].startswith('REJECT') for t in transcript)
    assert partition(selected,'independent') == 8
    print('selected:',selected)
    print('protocol transcript:')
    for x in transcript: print(' ',x)
    print('final observable Boolean predicates:',2**partition(selected,'independent'))
    print('PASS: baseline 2 -> validated 4 -> 8, artifact rejected')
if __name__=='__main__': check()
