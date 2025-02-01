from flet import *



SIZE_TEXT=30
DIR_FILE_ANSEWER_AND_INFOS="answer_and_info.txt"
DIR_FILE_TRUE_ANSWER="true_answer.txt"
TXT_ANSWER=""
TXT_TRUE_ANSWER=""
B_CORRECTION_CLICKED=None
DIC_ANSWER={"1":"0"  ,   "2":"1",   "3":"2"  ,  "4":"3"

            ,"1-2":"5"  ,   "1-3":"6"   ,  "1-4":"7" 

            ,"2-3":"8"  ,  "2-4":"9"

            ,  "3-4":"A"

            ,  "1-2-3":"B" ,  "1-2-4":"C" ,  "1-3-4":"D" ,  "2-3-4":"E"

            ,   "1-2-3-4":"F"
            , "":"-","-":"-"}

DIC_ANSWER_INV = dict(map(reversed, DIC_ANSWER.items()))


def write_answer_on_txt_file(n,answer):
    """n=str(n)
    if ".txt" not in n:
        dir_file_question=n+".txt"
    else :
        dir_file_question=n
    """
    #read txt file
    f=open(DIR_FILE_ANSEWER_AND_INFOS,"r")
    s=f.readlines()
    f.close()

    print(s)

    #replace answer of questioon number n
    new_answer=f"{n}:{answer}\n"
    s[int(n)]=new_answer
    

    #writeslines
    f=open(DIR_FILE_ANSEWER_AND_INFOS,"w")
    f.writelines(s)
    f.close()
    
    
        

def organizeAnswer(answer):
        answer_organiser=''
        answer=answer.replace(" ","")
        l=answer.split("-")
        while "" in l:
            l.remove("")
        for i in range(1,5):
            if str(i) in l:
                answer_organiser+=f"{i}-"
        answer_organiser=answer_organiser[:-1]
        if answer_organiser=="":
            answer_organiser="-"
        return answer_organiser

    

def on_click_principal(e,list_Buttons,text_answer,page,number_question):
        print("on_click_principal")
        val = e.control.text
        index=int(val)-1
        B=list_Buttons[index]

        old_color=B.bgcolor

        if  old_color=="#ff585d" :
            new_color="blue"
        if  old_color=="blue" :
            new_color="#ff585d"    #ff585d    
            
        B.bgcolor=new_color 
        

        #generate answer
        answer=""
        for B  in list_Buttons  :
            if  B.bgcolor=="blue" :
                print(B.text)
                answer+=str(B.text)+"-"
        new_answer=organizeAnswer(answer)
        print(new_answer)

        

        #
        
        #answer_writed=
        
        write_answer_on_txt_file(number_question ,new_answer)

        #update text_answer
        #print(text_answer)
        text_answer.text=new_answer

        
        

        page.update()
        
        #print(old_color)

        











def main(page:Page):

    #functions
    def changeNumberSeire(e):
        new_serie = e.control.text
        #page.appbar.bgcolor="blue"
        #page.appbar.title=new_serie  page.appbar.title={'value': '1- السلسة', 'n': 'title'}
        page.appbar.title=Text(new_serie)#['value']=new_serie
        page.update()
        print(new_serie)
        #update correction if i am in correction
        if row_result_back.visible :
                    go_to_correction()
        page.update()

    def changeNumberQuestion(e):
        new_number_question = e.control.text
        #page.appbar.bgcolor="blue"
        #page.appbar.title=new_serie  page.appbar.title={'value': '1- السلسة', 'n': 'title'}
        #page.appbar.title=Text(new_serie)#['value']=new_serie
        #page.update()
        print(new_number_question)
        

    #on_click_1
    def on_click(e):
        number_question=int(B_number_question.text.split("-")[1])
        on_click_principal(e,list_Buttons,text_answer,page,number_question)

    def on_click_on_button_correction(e):
        global B_CORRECTION_CLICKED ,  TXT_ANSWER,TXT_TRUE_ANSWER
        n=int(e.control.text)
        
        if not  B_CORRECTION_CLICKED==None :
            i=int(B_CORRECTION_CLICKED.text)-1
            #print("TXT_ANSWER[i:i+1],TXT_TRUE_ANSWER[i:i+1] ",TXT_ANSWER[i:i+1],TXT_TRUE_ANSWER[i:i+1])
            if TXT_ANSWER[i:i+1]==TXT_TRUE_ANSWER[i:i+1]:
                B_CORRECTION_CLICKED.bgcolor='green'
            else :
                B_CORRECTION_CLICKED.bgcolor="red"
        
        #go_to_correction()

        B_CORRECTION_CLICKED=list_all_buttons_corrections[n-1]
        B_CORRECTION_CLICKED.bgcolor='blue'
        #write answer
        i=n-1
        text_answer_candidat_in_correction.text=f"{DIC_ANSWER_INV[TXT_ANSWER[i:i+1]]}"+" : "+" الاجوبة "
        text_true_answer_in_correction.text=f"{DIC_ANSWER_INV[TXT_TRUE_ANSWER[i:i+1]]}"+" : "+" التصحيح "
        if TXT_ANSWER[i:i+1]==TXT_TRUE_ANSWER[i:i+1]:
            text_answer_candidat_in_correction.bgcolor="green"
        else  :
            text_answer_candidat_in_correction.bgcolor="red"
        print('TXT_ANSWER : ' ,TXT_ANSWER) 
        page.update()

    def go_next_question(e):
        
        n=int(B_number_question.text.split("-")[1])
        
        
                
                
        if n<40 :
            #go_to_specific_question
            go_to_specific_question(n+1)
        else :
            if n==40 :
                go_to_correction()
                
            

        page.update()
        

            

    def go_previeous_question(e):
        print("go_previeous_question")
        n=int(B_number_question.text.split("-")[1])
        if n>1 :
            n-=1

        #go_to_specific_question
        go_to_specific_question(n)

    def on_click_B_number_question(e):
        txt=e.control.text
        print(txt)
        [PopupMenuItem(text=f"السؤال-{i+1}",on_click=changeNumberQuestion) for i in range(40) ]
        
        

    def go_to_specific_question(n):
        B_number_question.text=f"السؤال-{n}"
        

        #load answer
        #colrer all with red
        for B in list_Buttons  :B.bgcolor="#ff585d"

        #read anwer
        
        f=open(DIR_FILE_ANSEWER_AND_INFOS,"r")
        s=f.readlines()
        f.close()
        print('len(s) =',len(s))
        answer=s[int(n)].replace("\n","").split(":")[1].split("-") #40:-
        print(" answer and number question ",n,answer)
        for i in range(4):
            if f"{i+1}" in answer : 
                B=list_Buttons[i]
                B.bgcolor="blue"

        #update
        page.update()


    def changeWidget(e):
        print('changeWidget')
        
        index=int(e.control.selected_index)
        #hide_all()
        hide_all()
        
        if index==1 :
            
    
                print("visible")
                #page.add(column_answer,row_next_back)
                column_answer.visible=True
                row_next_back.visible=True
            

            
        else :
            #show
            row_copy_save.visible=True
            text_writre_trueAnswer.visible=True
        page.update()
        
        print("index",index)

    def command_ask_yesy_no_to_save(e):
        print('command_ask_yesy_no_to_save')
        page.open(alert_dialog_save)

    def command_save_no(e):
        print('command_save_no')
        page.close(alert_dialog_save)

    def command_save_yes(e):
        print('command_save_yes')
        page.close(alert_dialog_save)

        txt=text_writre_trueAnswer.value
        print("text copied" , txt)

        #write answer
        file_answer=DIR_FILE_TRUE_ANSWER
        f=open(file_answer,"w")
        f.write(txt)
        f.close()

    def paste_text(e):
        txt=page.get_clipboard()
        text_writre_trueAnswer.value=txt
        page.update()

    
            

    def analyser_file_answer_and_info():

        list_infos=["info:number_serie=1#number_question=1\n"]
        list_answer=[ f"{i}:-\n"  for i  in range(1,41)]
        list_=list_infos+list_answer
        f=open(DIR_FILE_ANSEWER_AND_INFOS,"w")
        f.writelines(list_)
        f.close()


    def go_serie_and_question_for_demarage():
        #read txt file
        try :
            f=open(DIR_FILE_ANSEWER_AND_INFOS,"r")
            s=f.readlines()
            f.close()

            #new_info=f"info:number_serie=3 #number_question=5\n"
            info=s[0].replace("\n","")
            number_serie_=int(info.split("#")[0].split("=")[1])
            number_question_=int(info.split("#")[1].split("=")[1])

            #go to question
            go_to_specific_question(number_question_)

            #got to serie
            new_serie=f"السلسلة- {number_serie_}"
            page.appbar.title=Text(new_serie)
        except :
            pass


    def go_to_correction():
        #hide_all
                global  TXT_ANSWER,TXT_TRUE_ANSWER

                #hna khask tkhwi hado bach matb9ach ghir katzid fihom
                TXT_ANSWER=""
                TXT_TRUE_ANSWER=""
                
                hide_all()
                #show
                for row_corr in list_rows_corrections :
                    row_corr.visible=True

                #show
                row_result_back.visible=True

                #divider
                divider_0.visible=True
                divider.visible=True

                

                #show  row_answer_and_true_answer
                row_answer_and_true_answer.visible=True

                #color buttons  rja3
                #get all answer  as text like : 1AB11AB11AB11AB11AB11AB11AB11AB11AB11AB1
                #read answer
                f=open(DIR_FILE_ANSEWER_AND_INFOS,"r")
                s=f.readlines()
                f.close()

                #get number serie
                number_serie_=page.appbar.title.value.split('-')[0]
                if "س" in number_serie_ :
                    number_serie_=page.appbar.title.value.split('-')[1]
                    
                
                for i in range(1,41):
                    answer_=s[i].replace("\n","").split(":")[1]
                    
                    TXT_ANSWER+=DIC_ANSWER[answer_]
                #print(TXT_ANSWER)  

                #extact true answer
                f=open(DIR_FILE_TRUE_ANSWER,"r")
                s_corrections=f.readlines()
                f.close()

                for line_txt_true_answer in s_corrections :
                    if "#" in line_txt_true_answer :
                        number_serie_in_line_true_answer=int(line_txt_true_answer.split("#")[0])
                        if  int(number_serie_)==int(number_serie_in_line_true_answer):
                            TXT_TRUE_ANSWER=line_txt_true_answer.split("#")[1]
                #print(TXT_TRUE_ANSWER)

                #colorer  buttons
                count_result=0
                for i in range(40):
                    _answer=TXT_ANSWER[i:i+1]
                    _answer_true=TXT_TRUE_ANSWER[i:i+1]
                    #print("_answer  and _answer_true : " ,_answer, _answer_true)
                    if  _answer==_answer_true :
                        list_all_buttons_corrections[i].bgcolor='green'
                        count_result+=1
                    else :
                        list_all_buttons_corrections[i].bgcolor='red'

                #write result  yyyy
                text_result.text="النتيجة : "+f"{count_result}/40"
                if  count_result<32 :
                    text_result.bgcolor="red"
                if  count_result>31 :
                    text_result.bgcolor="green"

                #page
                page.update()
                    
                
                
                    


    def command_b_back_to_answer(e):
        #hide_all
        hide_all()
        

        #show   column_answer  and   row_next_back
        column_answer.visible=True
        row_next_back.visible=True
        

        #page.update()
        page.update()
        

    def hide_all():
        #hide
        row_copy_save.visible=False
        text_writre_trueAnswer.visible=False
            
        #hide   column_answer  and   row_next_back
        column_answer.visible=False
        row_next_back.visible=False
            
        #hide  all row in list_rows_corrections
        for row_corr in list_rows_corrections :
                    row_corr.visible=False
        #hide row_result_back
        row_result_back.visible=False

        #row_answer_and_true_answer
        row_answer_and_true_answer.visible=False

        #divider
        divider_0.visible=False
        divider.visible=False

        page.update()
        

    #demarage
    def demarage():
        #go_serie_and_question_for_demarage
        go_serie_and_question_for_demarage()
        #load answer
        #read answer
        file_answer=DIR_FILE_TRUE_ANSWER
        try :
            f=open(file_answer,"r")
            s=f.read()
            f.close()
            #write answer on text_writre_trueAnswer
            text_writre_trueAnswer.value=s
        except :
            f=open(file_answer,"w")
            f.close()
        #page.update()
        page.update()

        #creat file DIR_FILE_ANSEWER_AND_INFOS if not exist
        try :
            f=open(DIR_FILE_ANSEWER_AND_INFOS,"r")
            s=f.readlines()
            f.close()
            if  "info:number_serie" not in s[0] :
                analyser_file_answer_and_info()
                
        except :
            analyser_file_answer_and_info()

    #close_app
    def close_app(e):
        if e.data == "close":
            page.window.destroy()
            print("close_app")

            #get number serie
            str_number_serie=page.appbar.title.value.split('-')[0]
            if "س" in str_number_serie :
                str_number_serie=page.appbar.title.value.split('-')[1]
            print("number_serie : ",str_number_serie)

            #get number quesion rja3
            str_number_question=B_number_question.text.split("-")[1]
            if "س" in str_number_question :
                str_number_question=B_number_question.text.split("-")[0]
                

            print("str_number_question : ",str_number_question)

            new_info=f"info:number_serie={str_number_serie}#number_question={str_number_question}\n"
            print(new_info)

            #write info in txt file : DIR_FILE_ANSEWER_AND_INFOS

            #read txt file
            f=open(DIR_FILE_ANSEWER_AND_INFOS,"r")
            s=f.readlines()
            f.close()


            #replace new_info
            s[0]=new_info
            

            #writeslines
            f=open(DIR_FILE_ANSEWER_AND_INFOS,"w")
            f.writelines(s)
            f.close()
            
            
            

    
        
        

    
        
        

    
    
    page.title="Code Maroc Android"
    page.horizontal_alignment="center"
    page.vertical_alignment="center"
    #page.vertical_alignment = MainAxisAlignment.CENTER
    #page.horizontal_alignment = MainAxisAlignment.CENTER
    #page.padding=200
    
    



    #app appbar_seire
    page.appbar=AppBar(bgcolor="red",
                       
                       
                       title=Text("1- السلسة"),
                       center_title=True,
                       

                       actions=[
                           PopupMenuButton(
                               items=[
                                PopupMenuItem(text=f"السلسلة-{i+1}",on_click=changeNumberSeire) for i in range(40)])
                           ]
                       ,

                       #title=Text("1- السلسة"),
                       
                       
                       

                       )


    #navigation_bar
    page.navigation_bar=NavigationBar(height=60,
        on_change=changeWidget,
        selected_index=0,
        destinations=[
            NavigationBarDestination(icon=Icons.EDIT_DOCUMENT),
            NavigationBarDestination(icon=Icons.HOME)
            ]
        )


    
    
    B_with=300
    B_hieght=60
    B_number_question = FilledButton(text="السؤال-1",bgcolor="black",color="white",width=B_with, height=50
                                     ,on_click=on_click_B_number_question)

    #
    text_answer=TextButton(text="-", width=B_with, height=50)

    B1=FilledButton(text="1",bgcolor="#ff585d",width=B_with,height=B_hieght,on_click=on_click)
    B2=FilledButton(text="2",bgcolor="#ff585d",width=B_with,height=B_hieght,on_click=on_click)
    B3=FilledButton(text="3",bgcolor="#ff585d",width=B_with,height=B_hieght,on_click=on_click)
    B4=FilledButton(text="4",bgcolor="#ff585d",width=B_with,height=B_hieght,on_click=on_click)
    list_Buttons=[B1,B2,B3,B4]
    
    list_number_question_text_answser=[B_number_question,text_answer]

    B_back=FilledButton(text="<",bgcolor="black",color="white",width=int(B_with/2)-10
                        ,on_click=go_previeous_question)
    B_next=FilledButton(text=">",bgcolor="black",color="white",width=int(B_with/2)-10
                        ,on_click=go_next_question)
    #row_next_back
    row_next_back=Row(spacing=20, controls=[B_back,B_next],alignment="center")

    column_answer=Column(spacing=20, controls=list_number_question_text_answser+list_Buttons                         
                        )


    #TextAnswer
    text_writre_trueAnswer=TextField(multiline=True,min_lines=7,max_lines=7,width=400)
    
    #B_copy
    B_copy=FilledButton(text="نسخ",on_click=paste_text)

    
        

    #material_actions 
    material_actions = [
        TextButton(text="نعم",on_click=command_save_yes),
        TextButton(text="لا" , on_click=command_save_no),
    ]
    #B_save
    alert_dialog_save=AlertDialog(
                    title=Text("حفظ"),content=Text("هل تريد الحفظ ؟"),
                    actions=material_actions
                    )

    
        
    
    B_save=FilledButton(text="حفظ",on_click=command_ask_yesy_no_to_save)

    row_copy_save=Row(spacing=20, controls=[B_save,B_copy],alignment="center")

    
    

    
    #hide
    row_copy_save.visible=False
    text_writre_trueAnswer.visible=False


    #row_answer_and_true_answer
      
    

    text_answer_candidat_in_correction=FilledButton(text="الاجوبة : 1-2",bgcolor='red', width=63*2)

    text_true_answer_in_correction=FilledButton(text="التصحيح: 1-2-3-4",bgcolor='green', width=63*2)

    row_answer_and_true_answer=Row(spacing=10, controls=[text_true_answer_in_correction
                                                         ,text_answer_candidat_in_correction],alignment="center")
    row_answer_and_true_answer.visible=False

    page.add(row_answer_and_true_answer)
    #divider_0
    divider_0=Divider(height=1, color="black")
    divider_0.visible=False
    page.add(divider_0)


    

    #buttons corrections
    
    list_all_buttons_corrections=[]
    for i in range(40):
            b_correction=FilledButton(text=str(i+1),width=45 ,height=40,bgcolor="blue",on_click=on_click_on_button_correction)
            list_all_buttons_corrections.append(b_correction)

    #list_rows_corrections
    list_rows_corrections=[]
    for j in range(8):
        row_correction=Row(spacing=10, controls=list_all_buttons_corrections[5*j:5*j+5],alignment="center")
        list_rows_corrections.append(row_correction)
        row_correction.visible=False
        page.add(row_correction)

    #divider
    divider=Divider(height=1, color="black")
    divider.visible=False
    page.add(divider)
        
    #row_result_back
    b_back_to_answer=FilledButton(text="<",bgcolor="black",color="white", width=63*2
                        ,on_click=command_b_back_to_answer)

    text_result=FilledButton(text="النتيجة : 40/40",bgcolor='green', width=63*2)
    row_result_back=Row(spacing=10, controls=[b_back_to_answer,text_result],alignment="center")
    row_result_back.visible=False

    
    
    
    

    #add
    page.add(column_answer,row_next_back,text_writre_trueAnswer,row_copy_save,row_result_back)
    
    



    #call demarage()
    demarage()

    #event close
    page.window.prevent_close = True
    page.window.on_event = close_app
    
    #page.fullscreen=True
    page.update()


app(main)
