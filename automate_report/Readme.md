# Automasi Report Dashboard

Goal :
1. Data Sales Bulanan yang di output
2. Send ke Slack channel (platform kolaborasi team)
3. Goal : Team terkait bisa melihat report regular bulanan

Steps :
1. `pip install -r requirements.txt`
2. Buatlah `.env` file di dalam directory `plugins/send_to_slack`
3. Isilah `.env` dengan konten berikut SLACK_TOKEN='your-slack-token'
4. Jalankan `python report.py` untuk mengirim grafik ke Slack Channel