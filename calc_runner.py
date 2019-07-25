from calculator import KRACalculator

sal = KRACalculator('Keith', 30000, 0)

print('Name: ', sal.name)
print('Gross Salary: KSH', sal.gross_salary)
print('Taxable income: KSH', sal.taxable_income)
print('NSSF DEDUCTION: KSH', round(sal.NSSF, 2))
print('PAYE: KSH', round(sal.PAYE, 2))
print('Personal Relief: KSH', sal.personal_relief)
print('TAX NET OFF RELIEF: KSH', round(sal.after_relief, 2))
print('NHIF: KSH', sal.NHIF)
print('Net Salary: KSH',round(sal.net_salary, 2))