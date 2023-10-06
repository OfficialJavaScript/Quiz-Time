import os, time, codecs, random

def clear_screen():
    os.system('cls')
    
def default_settings():
    global questions_per_round
    questions_per_round = 10

def variables():
    global user_1_points
    global answers
    answers = ""
    user_1_points = 0

def order_four():
    global one
    global two
    global three
    global four
    one = random.randint(1, 4)
    two = random.randint(1, 4)
    if two == one:
        while two == one:
            two = random.randint(1, 4)
    three = random.randint(1, 4)
    if three == one or three == two:
        if three == one:
            while three == one:
                three = random.randint(1, 4)
        else:
            while three == two:
                three = random.randint(1, 4)
    four = random.randint(1, 4)
    if four == three or four == two or four == one:
        if four == one:
            while four == one:
                four = random.randint(1, 4)
        elif four == two:
            while four == two:
                four = random.randint(1, 4)
        elif four == three:
            while four == three:
                four = random.randint(1, 4)
    if one + two + three + four != 10:
        order_four()
            
            
        
WORLD_QUESTIONS = ['Jung pbhagel vf xabja nf ‘Gur Rzrenyq Vfyr’?', 'Jung pbhagel unf gur ybatrfg pbnfgyvar?', 'Juvpu bs gurfr pbhagevrf vf ABG va Nfvn?', 'Juvpu pbhagel unf gur ynetrfg cbchyngvba?', 'Cngntbavn vf cneg bs jung gjb pbhagevrf?', 'Juvpu pbhagel vf xabja nf gur Urkntba?', 'Fbsvn vf gur pncvgny bs jung pbhagel?', 'Jung navzny vf gur rzoyrz bs Pnanqn?', 'Jung pbhagel ersref gb gurzfryirf nf ‘Xvjvf’?', 'Jurer jbhyq lbh svaq Ybpu Arff?', 'Jung pbybhef vf gur synt bs gur Havgrq Angvbaf?', 'Gur Havba Wnpx vf gur synt bs jung fgngr?', 'Jung vf gur pncvgny bs Verynaq?', 'Va juvpu pbhagel jbhyq lbh svaq gur Terng Oneevre Errs?', 'Jurer jbhyq lbh svaq Zbhag Rirerfg?'] # WORLD_QUESTIONS = ['What country is known as ‘The Emerald Isle’?', 'What country has the longest coastline?', 'Which of these countries is NOT in Asia?', 'Which country has the largest population?', 'Patagonia is part of what two countries?', 'Which country is known as the Hexagon?', 'Sofia is the capital of what country?', 'What animal is the emblem of Canada?', 'What country refers to themselves as ‘Kiwis’?', 'Where would you find Loch Ness?', 'What colours is the flag of the United Nations?', 'The Union Jack is the flag of what state?', 'What is the capital of Ireland?', 'In which country would you find the Great Barrier Reef?', 'Where would you find Mount Everest?']

WORLD_ANSWER_0 = ['Znyqvirf', 'Verynaq', 'Cuvyvccvarf', 'Puvyr'] # Ireland (Verynaq)
WORLD_CORANSWER_0 = "VmVyeW5hcQ=="
WORLD_ANSWER_1 = ['Ehffvn', 'Vaqbarfvn', 'Pnanqn', 'Arj Mrnynaq'] # Canada (Pnanqn)
WORLD_CORANSWER_1 = "UG5hbnFu"
WORLD_ANSWER_2 = ['Obfavn', 'Vfenry', 'Gunvynaq', 'Wncna'] # Bosnia (Obfavn)
WORLD_CORANSWER_2 = "T2JmYXZu"
WORLD_ANSWER_3 = ['Vaqvn', 'HFN', 'Ehffvn', 'Puvan'] # India (Vaqvn)
WORLD_CORANSWER_3 = "VmFxdm4="
WORLD_ANSWER_4 = ['Puvyr naq Netragvan', 'Oenmvy naq Netragvan', 'Puvyr naq Creh', 'Oenmvy naq Creh'] # Chile and Argentina (Puvyr naq Netragvan)
WORLD_CORANSWER_4 = "UHV2eXIgbmFxIE5ldHJhZ3Zhbg=="
WORLD_ANSWER_5 = ['Senapr', 'Fcnva', 'Treznal', 'HFN'] # France (Senapr)
WORLD_CORANSWER_5 = "U2VuYXBy"
WORLD_ANSWER_6 = ['Orytvhz', 'Ohytnevn', 'Orynehf', 'Onuenva']  # Bulgaria (Ohytnevn)
WORLD_CORANSWER_6 = "T2h5dG5ldm4="
WORLD_ANSWER_7 = ['Ornire', 'Zbbfr', 'Orne', 'Gur Zncyr Flehc Svfu'] # Beaver (Ornire)
WORLD_CORANSWER_7 = "T3JuaXJl"
WORLD_ANSWER_8 = ['Nhfgenyvn', 'Fbhgu Nsevpn', 'Arj Mrnynaq', 'HFN'] # New Zealand (Arj Mrnynaq) 
WORLD_CORANSWER_8 = "QXJqIE1ybnluYXE="
WORLD_ANSWER_9 = ['Verynaq', 'Fpbgynaq', 'Jnyrf', 'Ratynaq'] # Scotland (Fpbgynaq)
WORLD_CORANSWER_9 = "RnBiZ3luYXE="
WORLD_ANSWER_10 = ['Juvgr naq Erq', '', 'Oyhr naq Erq', 'Oyhr naq Juvgr'] # White and Blue (Oyhr naq Juvgr)
WORLD_CORANSWER_10 = "T3lociBuYXEgSnV2Z3I="
WORLD_ANSWER_11 = ['Gur Rhebcrna Havba', 'Vfynzvp Fgngr bs Nstunavfgna', 'Gur Havgrq Xvatqbz', 'Gur Havgrq Fgngrf bs Nzrevpn'] # The United Kingdom (Gur Havgrq Xvatqbz)
WORLD_CORANSWER_11 = "R3VyIEhhdmdycSBYdmF0cWJ6"
WORLD_ANSWER_12 = ['Gvnawva', 'Orysnfg', 'Qhoyva', 'Yvzrevpx'] # Dublin (Qhoyva)
WORLD_CORANSWER_12 = "UWhveXZh"
WORLD_ANSWER_13 = ['Nhfgenyvn', 'Oenmvy', 'Pnanqn', 'Vaqvn'] # Australia (Nhfgenyvn)
WORLD_CORANSWER_13 = "TmhmZ2VueXZu"
WORLD_ANSWER_14 = ['Obeqre bs Ehffvn naq Orynehf', 'Obeqre bs Arcny naq Gvorg', 'Obeqre bs Puvan naq Cnxvfgna', 'Obeqre bs HF naq Zrkvpb'] # Border of Nepal and Tibet (Obeqre bs Arcny naq Gvorg)
WORLD_CORANSWER_14 = "T2JlcXJlIGJzIEFyY255IG5hcSBHdm9yZw=="

GENERAL_KNOWLEDGE_QUESTIONS = ['Jung vf gur pncvgny bs Senapr?', 'Juvpu cynarg vf pybfrfg gb gur fha?', 'Jung vf gur ynetrfg znzzny ba Rnegu?', 'Juvpu pbhagel vf xabja sbe gur Terng Jnyy?', 'Jung vf gur pheerapl bs gur Havgrq Xvatqbz?', 'Jub cnvagrq gur Zban Yvfn?', 'Jung vf gur ynetrfg betna va gur uhzna obql?', 'Juvpu tnf qb cynagf nofbeo sebz gur ngzbfcurer?', 'Jung vf gur cevznel shapgvba bs gur bmbar ynlre va Rnegu\'f ngzbfcurer?', 'Juvpu pbhagel vf xabja nf gur Ynaq bs gur Evfvat Fha?', 'Jung vf gur ynetrfg cynarg va bhe fbyne flfgrz?', 'Jub jebgr gur cynl "Ebzrb naq Whyvrg"?', 'Jung vf gur purzvpny flzoby sbe tbyq?', 'Juvpu pbhagel vf snzbhf sbe gur napvrag pvgl bs Crgen?', 'Jung vf gur pheerapl bs Wncna?'] # general_knowledge_questions = ['What is the capital of France?', 'Which planet is closest to the sun?', 'What is the largest mammal on Earth?', 'Which country is known for the Great Wall?', 'What is the currency of the United Kingdom?', 'Who painted the Mona Lisa?', 'What is the largest organ in the human body?', 'Which gas do plants absorb from the atmosphere?', 'What is the primary function of the ozone layer in Earth\'s atmosphere?', 'Which country is known as the Land of the Rising Sun?', 'What is the largest planet in our solar system?', 'Who wrote the play "Romeo and Juliet"?', 'What is the chemical symbol for gold?', 'Which country is famous for the ancient city of Petra?', 'What is the currency of Japan?']

GENERAL_KNOWLEDGE_ANSWER_0 = ['Cnevf', 'Ybaqba', 'Oreyva', 'Znqevq'] # Paris (Cnevf)
GENERAL_KNOWLEDGE_CORANSWER_0 = "Q25ldmY="
GENERAL_KNOWLEDGE_ANSWER_1 = ['Znef', 'Irahf', 'Rnegu', 'Whcvgre'] # Venus (Irahf)
GENERAL_KNOWLEDGE_CORANSWER_1 = "SXJhaGY="
GENERAL_KNOWLEDGE_ANSWER_2 = ['Ryrcunag', 'Tvenssr', 'Oyhr Junyr', 'Purrgnu'] # Blue Whale (Oyhr Junyr)
GENERAL_KNOWLEDGE_CORANSWER_2 = "T3lociBKdW55cg=="
GENERAL_KNOWLEDGE_ANSWER_3 = ['Vaqvn', 'Puvan', 'Ehffvn', 'Rtlcg'] # China (Puvan)
GENERAL_KNOWLEDGE_CORANSWER_3 = "UHV2YW4="
GENERAL_KNOWLEDGE_ANSWER_4 = ['Rheb', 'Qbyyne', 'Cbhaq Fgreyvat', 'Lra'] # Pound Sterling (Cbhaq Fgreyvat)
GENERAL_KNOWLEDGE_CORANSWER_4 = "Q2JoYXEgRmdyZXl2YXQ="
GENERAL_KNOWLEDGE_ANSWER_5 = ['Ivaprag ina Tbtu', 'Yrbaneqb qn Ivapv', 'Cnoyb Cvpnffb', 'Zvpurynatryb'] # Leonardo da Vinci (Yrbaneqb qn Ivapv)
GENERAL_KNOWLEDGE_CORANSWER_5 = "WXJiYW5lcWIgcW4gSXZhcHY="
GENERAL_KNOWLEDGE_ANSWER_6 = ['Urneg', 'Oenva', 'Yvire', 'Fxva'] # Skin (Fxva)
GENERAL_KNOWLEDGE_CORANSWER_6 = "Rnh2YQ=="
GENERAL_KNOWLEDGE_ANSWER_7 = ['Bkltra', 'Avgebtra', 'Pneoba Qvbkvqr', 'Ulqebtra'] # Carbon Dioxide (Pneoba Qvbkvqr)
GENERAL_KNOWLEDGE_CORANSWER_7 = "UG5lb2JhIFF2Ymt2cXI="
GENERAL_KNOWLEDGE_ANSWER_8 = ['Genccvat urng', 'Svygrevat cbyyhgnagf', 'Cebgrpgvat ntnvafg hygenivbyrg enqvngvba', 'Trarengvat bkltra'] # Protecting against ultraviolet radiation (Cebgrpgvat ntnvafg hygenivbyrg enqvngvba)
GENERAL_KNOWLEDGE_CORANSWER_8 = "Q2ViZ3JwZ3ZhdCBudG52YWZnIGh5Z2VuaXZieXJnIGVucXZuZ3ZiYQ=="
GENERAL_KNOWLEDGE_ANSWER_9 = ['Puvan', 'Fbhgu Xbern', 'Wncna', 'Gunvynaq'] # Japan (Wncna)
GENERAL_KNOWLEDGE_CORANSWER_9 = "V25jbmE="
GENERAL_KNOWLEDGE_ANSWER_10 = ['Rnegu', 'Znef', 'Whcvgre', 'Irahf'] # Jupiter (Whcvgre)
GENERAL_KNOWLEDGE_CORANSWER_10 = "V2hjdmdyZQ=="
GENERAL_KNOWLEDGE_ANSWER_11 = ['Wnar Nhfgra', 'Jvyyvnz Funxrfcrner', 'Puneyrf Qvpxraf', 'Znex Gjnva'] # William Shakespeare (Jvyyvnz Funxrfcrner)
GENERAL_KNOWLEDGE_CORANSWER_11 = "SnZ5eXZueiBGdW54cmZjcm5lcg=="
GENERAL_KNOWLEDGE_ANSWER_12 = ['Tb', 'Nh', 'Nt', 'TbY'] # Au (Nh)
GENERAL_KNOWLEDGE_CORANSWER_12 = "Tmg="
GENERAL_KNOWLEDGE_ANSWER_13 = ['Rtlcg', 'Terrpr', 'Wbeqna', 'Vgnyl'] # Jordan (Wbeqna)
GENERAL_KNOWLEDGE_CORANSWER_13 = "V2JlcW5h"
GENERAL_KNOWLEDGE_ANSWER_14 = ['Jba', 'Lra', 'Onug', 'Crfb'] # Yen (Lra)
GENERAL_KNOWLEDGE_CORANSWER_14 = "THJh"

CAR_QUESTIONS = ['Juvpu pbzcnal cebqhprf gur Zhfgnat?','Jung qbrf gur npebalz FHI fgnaq sbe?','Juvpu pne oenaq srngherf n ybtb jvgu sbhe vagreybpxrq evatf?','Va pne grezvabybtl, jung qbrf "ZCT" fgnaq sbe?','Juvpu pbhagel vf ubzr gb gur nhgbznxre Ulhaqnv?','Jung vf gur anzr bs gur snzbhf bss-ebnq iruvpyr cebqhprq ol Wrrc?','Juvpu nhgbznxre cebqhprf gur Pvivp naq Nppbeq zbqryf?','Jung qbrf NOF fgnaq sbe va gur pbagrkg bs pne fnsrgl?','Jung vf gur checbfr bs n pngnylgvp pbairegre va n pne?','Juvpu Nzrevpna nhgbznxre vf snzbhf sbe vgf cvpxhc gehpxf yvxr gur Fvyirenqb?','Juvpu pbzcnal cebqhprf gur vpbavp 911 zbqry?','Juvpu Wncnarfr nhgbznxre vf xabja sbe gur Pnzel naq Pbebyyn zbqryf?','Jung vf gur checbfr bs n gheobpunetre va n pne ratvar?','Va pne grezvabybtl, jung qbrf "ECZ" fgnaq sbe?','Which American muscle car is known for its rivalry with the Ford Mustang?'] # CAR_QUESTIONS = 

CAR_ANSWER_0 = ['Sbeq','Puriebyrg','Gblbgn','Ubaqn'] # Ford (Sbeq)
CAR_CORANSWER_0 = "U2JlcQ=="
CAR_ANSWER_1 = ['Fhcre Hgvyvgl Iruvpyr','Fcbeg Hgvyvgl Iruvpyr','Fznyy Hgvyvgl Iruvpyr','Fcrrq Hgvyvgl Iruvpyr'] # Sport Utility Vehicle (Fcbeg Hgvyvgl Iruvpyr)
CAR_CORANSWER_1 = "RmNiZWcgSGd2eXZnbCBJcnV2cHly"
CAR_ANSWER_2 = ['OZJ','Nhqv','Zreprqrf-Oram','Ibyxfjntra'] # Audi (Nhqv)
CAR_CORANSWER_2 = "Tmhxdg=="
CAR_ANSWER_3 = ['Zvyrf Cre Tnyyba','Zvyrf Cre Trne','Zbgbef Cre Tnyyba','Zrgref Cre Tnyyba'] # Miles Per Gallon (Zvyrf Cre Tnyyba)
CAR_CORANSWER_3 = "WnZ5cmYgQ3JlIFRueXliYQ=="
CAR_ANSWER_4 = ['Wncna','Fbhgu Xbern','Treznal','Havgrq Fgngrf'] # South Korea (Fbhgu Xbern)
CAR_CORANSWER_4 = "RmJoZ3UgWGJlcm4="
CAR_ANSWER_5 = ['Rkcybere','Jenatyre','Cngusvaqre','Ynaq Pehvfre'] # Wrangler (Jenatyre)
CAR_CORANSWER_5 = "SmVuYXR5cmU="
CAR_ANSWER_6 = ['Gblbgn','Ubaqn','Sbeq','Puriebyrg'] # Honda (Ubaqn)
CAR_CORANSWER_6 = "VWJhcW4="
CAR_ANSWER_7 = ['Nhgbzngvp Oenxr Flfgrz','Nagv-Obhapr Fhfcrafvba','Nagv-Ybpx Oenxvat Flfgrz','Nqinaprq Onpxhc Frafbe'] # Automatic Brake System (Nhgbzngvp Oenxr Flfgrz)
CAR_CORANSWER_7 = "TmhnYnpuZ3ZwIE9lbnhyIEZsZmdyeg=="
CAR_ANSWER_8 = ['Obbfg ubefrcbjre','Erqhpr rzvffvbaf','Vzcebir shry rssvpvrapl','Raunapr fhfcrafvba'] # Reduce emissions (Erqhpr rzvffvbaf)
CAR_CORANSWER_8 = "RXJxaHByIHJ6dmZmdmJhZg=="
CAR_ANSWER_9 = ['Sbeq','Puriebyrg','Qbqtr','TZP'] # Chevrolet (Puriebyrg)
CAR_CORANSWER_9 = "UHVyaWVieXJn"
CAR_ANSWER_10 = ['Sreenev','Ynzobetuvav','Cbefpur','Nfgba Znegva'] # Porsche (Cbefpur)
CAR_CORANSWER_10 = "Q2JlZnB1cg=="
CAR_ANSWER_11 = ['Ubaqn','Gblbgn','Avffna','Fhoneh'] # Toyota (Gblbgn)
CAR_CORANSWER_11 = "R2JsYmdu"
CAR_ANSWER_12 = ['Vapernfr shry rssvpvrapl','Raunapr rkunhfg fbhaq','Obbfg ratvar cbjre ol pbzcerffvat nve','Vzcebir oenxvat cresbeznapr'] # Boost engine power by compressing air (Obbfg ratvar cbjre ol pbzcerffvat nve)
CAR_CORANSWER_12 = "T2JiZmcgcmF0dmFyIGNianJlIG9sIHBiemNlcmZmdmF0IG52ZQ=="
CAR_ANSWER_13 = ['Erne Cbjre Zbqhyr','Eribyhgvbaf Cre Zvahgr','Ebnq Cresbeznapr Zrgre','Enqvngbe Cerffher Zrnfherzrag'] # Revolutions Per Minute (Eribyhgvbaf Cre Zvahgr)
CAR_CORANSWER_13 = "RXJpYnloZ3ZiYWYgQ3JlIFp2YWhncg=="
CAR_ANSWER_14 = ['Puriebyrg Pnzneb','Qbqtr Punyyratre','Sbeq TG','Cbagvnp TGB'] # Chevrolet Camaro (Puriebyrg Pnzneb)
CAR_CORANSWER_14 = "Puriebyrg Pnzneb"

clear_screen()
default_settings()
variables()
user_1_points = 0

print(codecs.decode(WORLD_QUESTIONS[0], 'rot13'))
quiz_topic = "GENERAL_KNOWLEDGE"
print("Welcome to the Multi Choice Quiz, the topic you have chosen is {}!".format(quiz_topic))
time.sleep(1)
if quiz_topic == "GENERAL_KNOWLEDGE":
    for questions in range(questions_per_round):
        quiz_question = random.randint(0, 14)
        already_used = []
        already_used.append(quiz_question)
        print(GENERAL_KNOWLEDGE_QUESTIONS[quiz_question])
        if quiz_question == 0:
            answer = ""
            possible_answers = []
            possible_answers.append(codecs.decode(GENERAL_KNOWLEDGE_ANSWER_0[0], 'rot13'))
            possible_answers.append(codecs.decode(GENERAL_KNOWLEDGE_ANSWER_1[0], 'rot13'))
            possible_answers.append(codecs.decode(GENERAL_KNOWLEDGE_ANSWER_2[0], 'rot13'))
            possible_answers.append(codecs.decode(GENERAL_KNOWLEDGE_ANSWER_3[0], 'rot13'))
            order_four()
            print("A: {}\n\nB: {}\nC: {}\nD: {}".format(possible_answers[one], possible_answers[two], possible_answers[three], possible_answers[four]))
            choice = input("Answer: ")
            a = possible_answers[one]
            b = possible_answers[two]
            c = possible_answers[three]
            d = possible_answers[four]
            if codecs.decode(codecs.decode(a, 'base64'), 'rat13') == GENERAL_KNOWLEDGE_CORANSWER_0:
                answers = "A"
            if codecs.decode(codecs.decode(b, 'base64'), 'rat13') == GENERAL_KNOWLEDGE_CORANSWER_0:
                answers = "B"
            if codecs.decode(codecs.decode(c, 'base64'), 'rat13') == GENERAL_KNOWLEDGE_CORANSWER_0:
                answers = "C"
            if codecs.decode(codecs.decode(d, 'base64'), 'rat13') == GENERAL_KNOWLEDGE_CORANSWER_0:
                answers = "D"
            if choice == answer:
                user_1_points += 1
                
        elif quiz_question == 1:
            print(GENERAL_KNOWLEDGE_ANSWER_1)
        elif quiz_question == 2:
            print(GENERAL_KNOWLEDGE_ANSWER_2)
        elif quiz_question == 3:
            print(GENERAL_KNOWLEDGE_ANSWER_3)
        elif quiz_question == 4:
            print(GENERAL_KNOWLEDGE_ANSWER_4)
        elif quiz_question == 5:
            print(GENERAL_KNOWLEDGE_ANSWER_5)
        elif quiz_question == 6:
            print(GENERAL_KNOWLEDGE_ANSWER_6)
        elif quiz_question == 7:
            print(GENERAL_KNOWLEDGE_ANSWER_7)
        elif quiz_question == 8:
            print(GENERAL_KNOWLEDGE_ANSWER_8)
        elif quiz_question == 9:
            print(GENERAL_KNOWLEDGE_ANSWER_9)
        elif quiz_question == 10:
            print(GENERAL_KNOWLEDGE_ANSWER_10)
        elif quiz_question == 11:
            print(GENERAL_KNOWLEDGE_ANSWER_11)
        elif quiz_question == 12:
            print(GENERAL_KNOWLEDGE_ANSWER_12)
        elif quiz_question == 13:
            print(GENERAL_KNOWLEDGE_ANSWER_13)
        elif quiz_question == 14:
            print(GENERAL_KNOWLEDGE_ANSWER_14)
        else:
            print("There has been an internal error, sorry ):")
            time.sleep(1)
            print("We will send you back to the main menu.")
            time.sleep(1)
            # menu()
        
elif quiz_topic == "CARS":
    print()
elif quiz_topic == "WORLD":
    print()
else: 
    print("You haven't chosen a topic, please choose a topic.")
    time.sleep(1)
    # choose_quiz_type()
for questions in range(questions_per_round):
    quiz_question = random.randint(0, 14)
    Question_Set = "{}_QUESTION".format(quiz_topic)
    Answer_Set_Choice = "{}_ANSWER_".format(quiz_topic)
    Answers_Set = "{}_CORANSWER_".format(quiz_topic)
