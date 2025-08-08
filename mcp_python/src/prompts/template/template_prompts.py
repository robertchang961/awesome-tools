"""Template prompts."""


prompt_convert_to_markdown = """將指定檔案轉為 markdown 格式。\n
檔案名稱為： {filename}\n
建立一個檔案，完整地顯示全部的內容。\n
若為 [PDF, PPTX, DOCX]，則逐頁輸出，且表格內容請維持格式以表格輸出。"""
