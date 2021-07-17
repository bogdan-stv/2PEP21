import subprocess
from subprocess import run, Popen

result = run(['dir'], shell=True, text=True, capture_output=True)
# print(type(result))
# print(result.stdout)

# result = run(['ping','8.8.8.8'])
# print(type(result))
# print(result.stdout)

result = Popen(['ping', '8.8.4.4'], text=True, stdout=subprocess.PIPE)
stdout, stderr = result.communicate()
print(f'Stdout:{stdout}')
print(f'Stderr:{stderr}')
# print(type(result))
# print(result.stdout)




