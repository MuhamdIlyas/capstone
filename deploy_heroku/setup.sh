mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"181240000831@unisnu.ac.id\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml