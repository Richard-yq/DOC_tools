#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修復文件換行的工具
移除txt檔案中的所有換行符號，獲得乾淨的文字內容
"""

import os
import sys

def remove_newlines(input_file, output_file=None):
    """
    移除檔案中的所有換行符號
    
    Args:
        input_file (str): 輸入檔案路徑
        output_file (str, optional): 輸出檔案路徑，如果為None則覆蓋原檔案
    
    Returns:
        str: 處理後的文字內容
    """
    try:
        # 讀取原始檔案
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 移除所有換行符號，並用空格替換以避免單字黏在一起
        # 先處理 \r\n，再處理單獨的 \n 和 \r
        clean_content = content.replace('\r\n', ' ').replace('\n', ' ').replace('\r', ' ')

        # 將 [數字] 前面加換行符號（如果不是在行首）
        import re
        # 先移除多餘空格
        clean_content = re.sub(r'\s+', ' ', clean_content).strip()
        # 在 [數字] 前加換行（但行首的 [數字] 不加）
        clean_content = re.sub(r'(?<!^)\s*(\[\d+\])', r'\n\1', clean_content)
        
        # 決定輸出檔案路徑
        if output_file is None:
            output_file = input_file

        # 寫入處理後的內容
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(clean_content)
        
        print(f"✅ 成功處理檔案: {input_file}")
        print(f"📁 輸出檔案: {output_file}")
        print(f"📝 原始長度: {len(content)} 字元")
        print(f"🧹 處理後長度: {len(clean_content)} 字元")
        print(f"🗑️  移除了 {len(content) - len(clean_content)} 個換行符號")
        
        return clean_content
        
    except FileNotFoundError:
        print(f"❌ 錯誤: 找不到檔案 '{input_file}'")
        return None
    except Exception as e:
        print(f"❌ 處理檔案時發生錯誤: {str(e)}")
        return None

def main():
    """主函數"""
    if len(sys.argv) < 2:
        print("使用方式:")
        print("  python reference_kit.py <輸入檔案> [輸出檔案]")
        print("範例:")
        print("  python reference_kit.py input.txt                # 覆蓋原檔案")
        print("  python reference_kit.py input.txt output.txt     # 儲存到新檔案")
        return
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    # 檢查輸入檔案是否存在
    if not os.path.exists(input_file):
        print(f"❌ 錯誤: 檔案 '{input_file}' 不存在")
        return
    
    # 處理檔案
    result = remove_newlines(input_file, output_file)
    
    if result is not None:
        print("\n✨ 檔案處理完成！文字內容已變成一行連續的文字。")

if __name__ == "__main__":
    main()
