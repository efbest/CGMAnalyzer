git clone https://github.com/efbest/CGMAnalyzer.git
cd CGMAnalyzer
python -m venv cgm_env
source cgm_env/bin/activate
pip install -r requirements.txt
streamlit run app/app.py
