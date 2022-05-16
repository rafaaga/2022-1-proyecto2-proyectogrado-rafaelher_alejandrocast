from streamlit import bootstrap

real_script = 'view/MainView.py'

bootstrap.run(real_script, f'run.py {real_script}', [], {})
