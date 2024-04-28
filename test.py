import win32com.client as win32

hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
hwp.Open(r"D:\ResearchPaperRPA\논문 분석 양식.hwp")
hwp.PutFieldText("요약", "테스트")
hwp.Save()
hwp.Quit()
