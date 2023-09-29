import unittest

import employee_connected


class TestStringMethods(unittest.TestCase):
    def test_employee_connected_positive(self):
        emp_tree = {
            'name' : 'ceo_1',
            'reports' : [
                {
                    'name' : 'ceo_1_direct_report_1',
                    'reports' : []
                },
                {
                    'name' : 'ceo_1_direct_report_2',
                    'reports' : [
                        {
                            'name' : 'ceo_1_direct_report_2_direct_1',
                            'reports' :  []
                        }
                    ] # list ceo_1_direct_report_2_reports
                }
            ] # list_ceo1_reports
        }
        emp1_name = 'ceo_1_direct_report_2'
        emp2_name = 'ceo_1_direct_report_2_direct_1'
        found_emp1 = False
        found_emp2 = False
        self.assertTrue(employee_connected.search_employee_in_tree(emp_tree,
                                                                   emp1_name,
                                                                   emp2_name,
                                                                   found_emp1,
                                                                   found_emp2))

    def test_employee_connected_negative(self):
        emp_tree = {
            'name' : 'ceo_1',
            'reports' : [
                {
                    'name' : 'ceo_1_direct_report_1',
                    'reports' : []
                },
                {
                    'name' : 'ceo_1_direct_report_2',
                    'reports' : [
                        {
                            'name' : 'ceo_1_direct_report_2_direct_1',
                            'reports' :  []
                        }
                    ] # list ceo_1_direct_report_2_reports
                }
            ] # list_ceo1_reports
        }
        emp1_name = 'ceo_1_direct_report_2'
        emp2_name = 'whoami'
        found_emp1 = False
        found_emp2 = False
        self.assertFalse(employee_connected.search_employee_in_tree(emp_tree,
                                                                   emp1_name,
                                                                   emp2_name,
                                                                   found_emp1,
                                                                   found_emp2))


if __name__ == '__main__':
    unittest.main()