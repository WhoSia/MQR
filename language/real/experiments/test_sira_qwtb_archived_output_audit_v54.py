import unittest
from sira_qwtb_archived_output_audit_v54 import audit

def fixture():
    S=[1]
    for i in range(60):
        S.append(S[-1]+(12 if i%2==0 else 102))
    def mat(k,vals):
        return f'#startmatrix:: {k}\n    "[{",".join(map(str,vals))}]"\n#endmatrix:: {k}\n'
    qwtb=mat('M',[-1 if i%2==0 else 1 for i in range(60)])+mat('S',S)+mat('Uref',range(20))
    raw='; '.join(['1.0']*30)
    def section(k,v):
        return f'#startsection:: {k}\n#startmatrix:: value\n{v}\n#endmatrix:: value\n#endsection:: {k}\n'
    return qwtb,'uncertainty mode:: none\n'+section('U_t',raw)+section('U','1.0'),S[-1]-1


class TestArchiveGate(unittest.TestCase):
    def test_valid_synthetic_schedule(self):
        q,r,n=fixture(); x=audit(q,r,n)
        self.assertEqual(x['segments'],60)
        self.assertEqual(x['window_lengths'],{12:30,102:30})
        self.assertEqual(x['total_count'],n)
        self.assertEqual(x['paired_window_cycles'],30)

    def test_offset_sample_bounds_rejected(self):
        q,r,n=fixture()
        with self.assertRaises(ValueError):audit(q,r,n+1)

    def test_no_silent_window_label_mismatch(self):
        q,r,n=fixture()
        with self.assertRaises(ValueError):audit(q.replace('[-1,1,-1,1','[-1,-1,-1,1',1),r,n)

    def test_incorrect_result_aggregate_rejected(self):
        q,r,n=fixture()
        with self.assertRaises(ValueError):audit(q,r.replace('value\n1.0\n','value\n1.02\n'),n)

    def test_suspicious_uncertainty_annotation_rejected(self):
        q,r,n=fixture()
        with self.assertRaises(ValueError):audit(q,r.replace('uncertainty mode:: none','uncertainty mode:: propagation'),n)

    def test_partial_reference_vector_rejected(self):
        q,r,n=fixture()
        q=q.replace('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19','0,1,2')
        with self.assertRaises(ValueError):audit(q,r,n)

    def test_nonfinite_result_rejected(self):
        q,r,n=fixture()
        with self.assertRaises(ValueError):audit(q,r.replace('1.0; 1.0','nan; 1.0',1),n)

    def test_imperfect_hardware_boundary_accepted(self):
        q,r,n=fixture()
        q=q.replace('[1,13,115,127,229','[1,13,116,127,229',1)
        self.assertEqual(audit(q,r,n)['total_count'],n)

    def test_noninteger_boundary_rejected(self):
        q,r,n=fixture()
        q=q.replace('[1,13,115,127,229','[1,13.5,115,127,229',1)
        with self.assertRaises(ValueError):audit(q,r,n)


if __name__=='__main__':
    unittest.main()
