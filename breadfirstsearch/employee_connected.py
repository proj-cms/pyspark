import pprint
# emp structure
#{
#  'name' : 'ceo_1',
#  'reports' : [
#      {
#        'name' : 'ceo_1_direct_report_1'
#         'reports' : []
#      },
#      {
#        'name' : 'ceo_1_direct_report_2'
#        'reports' : [
#          {
#            'name' : 'ceo_1_direct_report_2_direct_1'
#            'reports' :  []
#          }
#        ] # list ceo_1_direct_report_2_reports
#      }
#  ] # list_ceo1_reports
#}
#


def search_employee_in_tree(emp_tree, emp1_name, emp2_name,found_emp1,found_emp2):
    if emp_tree['name'] == emp1_name:
        found_emp1 = True
    elif emp_tree['name'] == emp2_name:
        found_emp2 = True

    if found_emp2 and found_emp1:
        return True

    return any(search_employee_in_tree(j,emp1_name,emp2_name,found_emp1,found_emp2)
                 for j in emp_tree.get('reports',[]))


if __name__ == "__main__":
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
    pprint.PrettyPrinter(width=20).pprint(emp_tree)
    emp1_name = 'ceo_1_direct_report_2'
    emp2_name = 'ceo_1_direct_report_2_direct_1'
    #emp2_name = 'test'
    found_emp1 = False
    found_emp2 = False
    if search_employee_in_tree(emp_tree, emp1_name, emp2_name,found_emp1,found_emp2):
        print('Employees are under same ceo')
    else:
        print('Employees are not in same tree')