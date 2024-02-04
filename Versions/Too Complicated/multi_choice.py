import os, time, codecs, random, base64

def clear_screen():
    os.system('cls')
    
def default_settings():
    global questions_per_round
    questions_per_round = 10

def variables():
    global user_1_points
    global correct
    global incorrect
    global abcd
    global times_through
    global corrects
    user_1_points = 0
    correct = "Your answer is correct!!"
    incorrect = "Sorry, you got it incorrect."
    abcd = ['a', 'b', 'c', 'd']
    times_through = 0
    corrects = 0
    
def order_four():
    global one
    global two
    global three
    global four
    one = random.randint(0, 3)
    two = random.randint(0, 3)
    while two == one:
        two = random.randint(0, 3)
        if two != one:
            break
    three = random.randint(0, 3)
    while three == one or three == two:
        three = random.randint(0, 3)
        if three != one and three != two:
            break
    four = random.randint(0, 3)
    while four == one or four == two or four == three:
        four = random.randint(0, 3)
        if four != three and four != two and four != one:
            break
            
def decoder(answer_list, possible_answers):
    global answers
    a = possible_answers[one]
    b = possible_answers[two]
    c = possible_answers[three]
    d = possible_answers[four]
    to_be_decode = answer_list
    answer_list_decode = base64.b64decode(to_be_decode) 
    answer_list_decode = answer_list_decode.decode('UTF-8')
    if a == codecs.decode(answer_list_decode, 'rot13'):
        answers = "a"
        return answers
    if b == codecs.decode(answer_list_decode, 'rot13'):
        answers = "b"
        return answers
    if c == codecs.decode(answer_list_decode, 'rot13'):
        answers = "c"
        return answers
    if d == codecs.decode(answer_list_decode, 'rot13'):
        answers = "d"
        return answers

def possible_answers_function(answerset):
    global possible_answers
    possible_answers = []
    possible_answers.append(codecs.decode(answerset[0], 'rot13'))
    possible_answers.append(codecs.decode(answerset[1], 'rot13'))
    possible_answers.append(codecs.decode(answerset[2], 'rot13'))
    possible_answers.append(codecs.decode(answerset[3], 'rot13'))


def quiz_question_function(times_through, lists, quiz_question, answer_list, cor_answer):
    global user_1_points
    global corrects
    clear_screen()
    while True:
        # deepcode ignore single~iteration~loop: This is to stop Snyk (A security program) from complaining.
        print(codecs.decode(lists[quiz_question], 'rot13'))
        possible_answers_function(answer_list)
        order_four()
        print("A: {}\nB: {}\nC: {}\nD: {}".format(possible_answers[one], possible_answers[two], possible_answers[three], possible_answers[four]))
        choice = input("Answer: ") 
        decoder(cor_answer, possible_answers)
        choice = choice.lower()
        if choice.lower() == answers.lower():
            user_1_points += 1
            corrects += 1
            print(correct)
            time.sleep(1)
            break
        elif choice.lower() in abcd:
            print(incorrect)
            time.sleep(1)
            break
        else:
            print("{} is not a valid answer, please choose A, B, C, or D\n".format(choice))
        return times_through, corrects, user_1_points

    
        
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
GENERAL_KNOWLEDGE_ANSWER_1 = ['Znef', 'Irahf', 'Rnegu', 'Zrephel'] # Mercury (Zrephel)
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

CAR_QUESTIONS = ['Juvpu pbzcnal cebqhprf gur Zhfgnat?','Jung qbrf gur npebalz FHI fgnaq sbe?','Juvpu pne oenaq srngherf n ybtb jvgu sbhe vagreybpxrq evatf?','Va pne grezvabybtl, jung qbrf "ZCT" fgnaq sbe?','Juvpu pbhagel vf ubzr gb gur nhgbznxre Ulhaqnv?','Jung vf gur anzr bs gur snzbhf bss-ebnq iruvpyr cebqhprq ol Wrrc?','Juvpu nhgbznxre cebqhprf gur Pvivp naq Nppbeq zbqryf?','Jung qbrf NOF fgnaq sbe va gur pbagrkg bs pne fnsrgl?','Jung vf gur checbfr bs n pngnylgvp pbairegre va n pne?','Juvpu Nzrevpna nhgbznxre vf snzbhf sbe vgf cvpxhc gehpxf yvxr gur Fvyirenqb?','Juvpu pbzcnal cebqhprf gur vpbavp 911 zbqry?','Juvpu Wncnarfr nhgbznxre vf xabja sbe gur Pnzel naq Pbebyyn zbqryf?','Jung vf gur checbfr bs n gheobpunetre va n pne ratvar?','Va pne grezvabybtl, jung qbrf "ECZ" fgnaq sbe?','Juvpu Nzrevpna zhfpyr pne vf xabja sbe vgf evinyel jvgu gur Sbeq Zhfgnat?'] # CAR_QUESTIONS = 

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
CAR_CORANSWER_14 = "UHVyaWVieXJnIFBuem5lYg=="

TECHNOLOGY_QUESTIONS = ['Jung qbrf PCH fgnaq sbe?', 'Juvpu cebtenzzvat ynathntr vf xabja sbe vgf hfr va jro qrirybczrag naq vf bsgra rzorqqrq va UGZY pbqr?', 'Jung qbrf ENZ fgnaq sbe va n pbzchgre pbagrkg?', 'Juvpu bs gur sbyybjvat vf na rknzcyr bs na bcrengvat flfgrz?', 'Jung qbrf TCH fgnaq sbe?', 'Juvpu fgbentr qrivpr hfrf zntargvp fgbentr gb fgber qngn?', 'Va argjbexvat, jung qbrf YNA fgnaq sbe?', 'Jung vf gur checbfr bs gur OVBF va n pbzchgre?', 'Jung vf gur checbfr bs gur \'cvat\' pbzznaq va argjbexvat?', 'Jung vf gur shapgvba bs na Rgurearg cbeg ba n pbzchgre?', 'Jung qbrf HEY fgnaq sbe?', 'Juvpu bs gur sbyybjvat vf n glcr bs znyjner gung qvfthvfrf vgfrys nf yrtvgvzngr fbsgjner?', 'Jung vf gur checbfr bs gur Pgey + M xrlobneq fubegphg va znal nccyvpngvbaf?', 'Jung vf gur cevznel shapgvba bs gur QAF (Qbznva Anzr Flfgrz)?', 'Juvpu svyr rkgrafvba vf pbzzbayl hfrq sbe rkrphgnoyr svyrf va Jvaqbjf?']

TECHNOLOGY_ANSWER_0 = ['Prageny Cebprffvat Havg', 'Pbzchgre Cebprffvat Havg', 'Prageny Cevagrq Havg', 'Prageny Cbjre Havg'] # Central Processing Unit (Prageny Cebprffvat Havg)
TECHNOLOGY_CORANSWER_0 = "UHJhZ2VueSBDZWJwcmZmdmF0IEhhdmc="
TECHNOLOGY_ANSWER_1 = ['Wnin', 'Clguba', 'WninFpevcg', 'Ehol'] # Javascript (WninFpevcg)
TECHNOLOGY_CORANSWER_1 = "V25pbkZwZXZjZw=="
TECHNOLOGY_ANSWER_2 = ['Enaqbz Npprff Zrzbel', 'Ernq-Bayl Zrzbel', 'Encvq Nccyvpngvba Znantrzrag', 'Erzbgr Npprff Zbqhyr'] # Random Access Memory (Enaqbz Npprff Zrzbel)
TECHNOLOGY_CORANSWER_2 = "RW5hcWJ6IE5wcHJmZiBacnpiZWw="
TECHNOLOGY_ANSWER_3 = ['Zvpebfbsg Bssvpr', 'Yvahk', 'Nqbor Cubgbfubc', 'Tbbtyr Puebzr'] # Linux (Yvahk)
TECHNOLOGY_CORANSWER_3 = "WXZhaGs="
TECHNOLOGY_ANSWER_4 = ['Trareny Cebprffvat Havg', 'Tencuvpf Cebprffvat Havg', 'Tnzvat Cebprffvat Havg', 'Trareny Checbfr Havg'] # Graphics Processing Unit (Tencuvpf Cebprffvat Havg)
TECHNOLOGY_CORANSWER_4 = "VGVuY3V2cGYgQ2VicHJmZnZhdCBIYXZn"
TECHNOLOGY_ANSWER_5 = ['FFQ (Fbyvq Fgngr Qevir)', 'UQQ (Uneq Qvfx Qevir)', 'HFO Synfu Qevir', 'PQ-EBZ'] # HDD (Hard Disk Drive) (UQQ (Uneq Qvfx Qevir))
TECHNOLOGY_CORANSWER_5 = "VVFRIChVbmVxIFF2ZnggUWV2aXIp"
TECHNOLOGY_ANSWER_6 = ['Ybpny Npprff Argjbex', 'Ybat Nern Argjbex', 'Ybpny Nern Argjbex', 'Yvarne Nern Argjbex'] # Local Area Network (Ybpny Nern Argjbex)
TECHNOLOGY_CORANSWER_6 = "WWJwbnkgTmVybiBBcmdqYmV4"
TECHNOLOGY_ANSWER_7 = ['Gb fgber qngn creznaragyl', 'Gb znantr vachg qrivprf', 'Gb pbageby onfvp uneqjner shapgvbaf', 'Gb eha nccyvpngvbaf'] # To control basic hardware functions (Gb pbageby onfvp uneqjner shapgvbaf)
TECHNOLOGY_CORANSWER_7 = "R2IgcGJhZ2VieSBvbmZ2cCB1bmVxam5lciBzaGFwZ3ZiYWY="
TECHNOLOGY_ANSWER_8 = ['Gb fraq rznvyf', 'Gb grfg argjbex pbaarpgvivgl', 'Gb qbjaybnq svyrf sebz gur vagrearg', 'Gb rapelcg qngn genafzvffvba'] # To test network connectivity (Gb grfg argjbex pbaarpgvivgl)
TECHNOLOGY_CORANSWER_8 = "R2IgZ3JmZyBhcmdqYmV4IHBiYWFycGd2aXZnbA=="
TECHNOLOGY_ANSWER_9 = ['Gb pbaarpg gb n cbjre fbhepr', 'Gb pbaarpg gb gur vagrearg be n ybpny argjbex', 'Gb pbaarpg gb rkgreany fgbentr qrivprf', 'Gb pbaarpg gb n cevagre'] # To connect to the internet or a local network (Gb pbaarpg gb gur vagrearg be n ybpny argjbex)
TECHNOLOGY_CORANSWER_9 = "R2IgcGJhYXJwZyBnYiBndXIgdmFncmVhcmcgYmUgbiB5YnBueSBhcmdqYmV4"
TECHNOLOGY_ANSWER_10 = ['Havsbez Erfbhepr Ybpngbe', 'Havirefny Erfbhepr Ybpngbe', 'Havsvrq Erfbhepr Ybpngbe', 'Hfre Erfbhepr Ybpngbe'] # Uniform Resource Locator (Havsbez Erfbhepr Ybpngbe)
TECHNOLOGY_CORANSWER_10 = "SGF2c2JleiBFcmZiaGVwciBZYnBuZ2Jl"
TECHNOLOGY_ANSWER_11 = ['Fcljner', 'Nqjner', 'Gebwna Ubefr', 'Jbez'] # Trojan Horse (Gebwna Ubefr)
TECHNOLOGY_CORANSWER_11 = "R2Vid25hIFViZWZy"
TECHNOLOGY_ANSWER_12 = ['Pbcl', 'Cnfgr', 'Haqb', 'Erqb'] # Undo (Haqb)
TECHNOLOGY_CORANSWER_12 = "SGFxYg=="
TECHNOLOGY_ANSWER_13 = ['Gb pbaireg qbznva anzrf gb VC nqqerffrf', 'Gb rapelcg vagrearg pbzzhavpngvba', 'Gb fgber jrofvgr pbagrag', 'Gb pbageby vagrearg npprff'] # To convert domain names to IP addresses (Gb pbaireg qbznva anzrf gb VC nqqerffrf)
TECHNOLOGY_CORANSWER_13 = "R2IgcGJhaXJlZyBxYnpudmEgYW56cmYgZ2IgVkMgbnFxZXJmZnJm"
TECHNOLOGY_ANSWER_14 = ['.rkr', '.qbp', '.mvc', '.gkg'] # .exe (.rkr)
TECHNOLOGY_CORANSWER_14 = "LnJrcg=="

clear_screen()
default_settings()
variables()
times_through = 0
user_1_points = 0
name = "Seb"
quiz_topic = "TECHNOLOGY"
already_used = []
print("Welcome {} to the Multi Choice Quiz, the topic you have chosen is {}!".format(name, quiz_topic))
time.sleep(2)
if quiz_topic == "GENERAL_KNOWLEDGE":
    for questions in range(questions_per_round):
        quiz_question = random.randint(0, 14)
        times_through += 1
        while quiz_question in already_used:
            quiz_question = random.randint(0, 14)
            if quiz_question in already_used == False:
                break
        already_used.append(quiz_question)
        if quiz_question == 0:
            quiz_question_function(times_through, GENERAL_KNOWLEDGE_QUESTIONS, quiz_question, GENERAL_KNOWLEDGE_ANSWER_0, GENERAL_KNOWLEDGE_CORANSWER_0)
                
        elif quiz_question == 1:
            quiz_question_function(times_through, GENERAL_KNOWLEDGE_QUESTIONS, quiz_question, GENERAL_KNOWLEDGE_ANSWER_1, GENERAL_KNOWLEDGE_CORANSWER_1)
                
        elif quiz_question == 2:
            quiz_question_function(times_through, GENERAL_KNOWLEDGE_QUESTIONS, quiz_question, GENERAL_KNOWLEDGE_ANSWER_2, GENERAL_KNOWLEDGE_CORANSWER_2)
                    
        elif quiz_question == 3:
            quiz_question_function(times_through, GENERAL_KNOWLEDGE_QUESTIONS, quiz_question, GENERAL_KNOWLEDGE_ANSWER_3, GENERAL_KNOWLEDGE_CORANSWER_3)
                    
        elif quiz_question == 4:
            quiz_question_function(times_through, GENERAL_KNOWLEDGE_QUESTIONS, quiz_question, GENERAL_KNOWLEDGE_ANSWER_4, GENERAL_KNOWLEDGE_CORANSWER_4)
                    
        elif quiz_question == 5:
            quiz_question_function(times_through, GENERAL_KNOWLEDGE_QUESTIONS, quiz_question, GENERAL_KNOWLEDGE_ANSWER_5, GENERAL_KNOWLEDGE_CORANSWER_5)
            
        elif quiz_question == 6:
            quiz_question_function(times_through, GENERAL_KNOWLEDGE_QUESTIONS, quiz_question, GENERAL_KNOWLEDGE_ANSWER_6, GENERAL_KNOWLEDGE_CORANSWER_6)
                    
        elif quiz_question == 7:
            quiz_question_function(times_through, GENERAL_KNOWLEDGE_QUESTIONS, quiz_question, GENERAL_KNOWLEDGE_ANSWER_7, GENERAL_KNOWLEDGE_CORANSWER_7)
                    
        elif quiz_question == 8:
            quiz_question_function(times_through, GENERAL_KNOWLEDGE_QUESTIONS, quiz_question, GENERAL_KNOWLEDGE_ANSWER_8, GENERAL_KNOWLEDGE_CORANSWER_8)
            
        elif quiz_question == 9:
            quiz_question_function(times_through, GENERAL_KNOWLEDGE_QUESTIONS, quiz_question, GENERAL_KNOWLEDGE_ANSWER_9, GENERAL_KNOWLEDGE_CORANSWER_9)
            
        elif quiz_question == 10:
            quiz_question_function(times_through, GENERAL_KNOWLEDGE_QUESTIONS, quiz_question, GENERAL_KNOWLEDGE_ANSWER_10, GENERAL_KNOWLEDGE_CORANSWER_10)

        elif quiz_question == 11:
            quiz_question_function(times_through, GENERAL_KNOWLEDGE_QUESTIONS, quiz_question, GENERAL_KNOWLEDGE_ANSWER_11, GENERAL_KNOWLEDGE_CORANSWER_11)
                    
        elif quiz_question == 12:
            quiz_question_function(times_through, GENERAL_KNOWLEDGE_QUESTIONS, quiz_question, GENERAL_KNOWLEDGE_ANSWER_12, GENERAL_KNOWLEDGE_CORANSWER_12)
                    
        elif quiz_question == 13:
            quiz_question_function(times_through, GENERAL_KNOWLEDGE_QUESTIONS, quiz_question, GENERAL_KNOWLEDGE_ANSWER_13, GENERAL_KNOWLEDGE_CORANSWER_13)
                    
        elif quiz_question == 14:    
            quiz_question_function(times_through, GENERAL_KNOWLEDGE_QUESTIONS, quiz_question, GENERAL_KNOWLEDGE_ANSWER_14, GENERAL_KNOWLEDGE_CORANSWER_14)
            
        else:
            clear_screen()
            print("There has been an internal error, sorry ):")
            time.sleep(1)
            print("We will send you back to the main menu.")
            time.sleep(1)
            # menu()

    if corrects > times_through * 0.8:
        print("Well done {}!, You got {} out of {} Correct, thats {}% correct!".format(name, corrects, times_through, corrects / times_through * 100))
        
    elif corrects > times_through * 0.5:
        print("Nice job {}!, You got {} out of {} Correct, thats {}% correct!".format(name, corrects, times_through, corrects / times_through * 100))
        
    else:
        print("Nice try {}, You got out of {} Correct, thats {}% correct!, you'll do better next time!!".format(corrects, times_through, corrects / times_through * 100))
        
elif quiz_topic == "CARS":
    for questions in range(questions_per_round):
        quiz_question = random.randint(0, 14)
        times_through += 1
        while quiz_question in already_used:
            quiz_question = random.randint(0, 14)
            if quiz_question in already_used == False:
                break
        already_used.append(quiz_question)
        if quiz_question == 0:
            quiz_question_function(times_through, CAR_QUESTIONS, quiz_question, CAR_ANSWER_0, CAR_CORANSWER_0)
                
        elif quiz_question == 1:
            quiz_question_function(times_through, CAR_QUESTIONS, quiz_question, CAR_ANSWER_1, CAR_CORANSWER_1)
                
        elif quiz_question == 2:
            quiz_question_function(times_through, CAR_QUESTIONS, quiz_question, CAR_ANSWER_2, CAR_CORANSWER_2)
                    
        elif quiz_question == 3:
            quiz_question_function(times_through, CAR_QUESTIONS, quiz_question, CAR_ANSWER_3, CAR_CORANSWER_3)
                    
        elif quiz_question == 4:
            quiz_question_function(times_through, CAR_QUESTIONS, quiz_question, CAR_ANSWER_4, CAR_CORANSWER_4)
                    
        elif quiz_question == 5:
            quiz_question_function(times_through, CAR_QUESTIONS, quiz_question, CAR_ANSWER_5, CAR_CORANSWER_5)
            
        elif quiz_question == 6:
            quiz_question_function(times_through, CAR_QUESTIONS, quiz_question, CAR_ANSWER_6, CAR_CORANSWER_6)
                    
        elif quiz_question == 7:
            quiz_question_function(times_through, CAR_QUESTIONS, quiz_question, CAR_ANSWER_7, CAR_CORANSWER_7)
                    
        elif quiz_question == 8:
            quiz_question_function(times_through, CAR_QUESTIONS, quiz_question, CAR_ANSWER_8, CAR_CORANSWER_8)
            
        elif quiz_question == 9:
            quiz_question_function(times_through, CAR_QUESTIONS, quiz_question, CAR_ANSWER_9, CAR_CORANSWER_9)
            
        elif quiz_question == 10:
            quiz_question_function(times_through, CAR_QUESTIONS, quiz_question, CAR_ANSWER_10, CAR_CORANSWER_10)

        elif quiz_question == 11:
            quiz_question_function(times_through, CAR_QUESTIONS, quiz_question, CAR_ANSWER_11, CAR_CORANSWER_11)
                    
        elif quiz_question == 12:
            quiz_question_function(times_through, CAR_QUESTIONS, quiz_question, CAR_ANSWER_12, CAR_CORANSWER_12)
                    
        elif quiz_question == 13:
            quiz_question_function(times_through, CAR_QUESTIONS, quiz_question, CAR_ANSWER_13, CAR_CORANSWER_13)
                    
        elif quiz_question == 14:    
            quiz_question_function(times_through, CAR_QUESTIONS, quiz_question, CAR_ANSWER_14, CAR_CORANSWER_14)
            
        else:
            clear_screen()
            print("There has been an internal error, sorry ):")
            time.sleep(1)
            print("We will send you back to the main menu.")
            time.sleep(1)
            # menu()

    if corrects > times_through * 0.8:
        print("Well done {}!, You got {} out of {} Correct, thats {}% correct!".format(name, corrects, times_through, corrects / times_through * 100))
   
    elif corrects > times_through * 0.5:
        print("Nice job {}!, You got {} out of {} Correct, thats {}% correct!".format(name, corrects, times_through, corrects / times_through * 100))
    
    else:
        print("Nice try {}, You got out of {} Correct, thats {}% correct!, you'll do better next time!!".format(corrects, times_through, corrects / times_through * 100))
elif quiz_topic == "WORLD":
    for questions in range(questions_per_round):
        quiz_question = random.randint(0, 14)
        times_through += 1
        while quiz_question in already_used:
            quiz_question = random.randint(0, 14)
            if quiz_question in already_used == False:
                break
        already_used.append(quiz_question)
        if quiz_question == 0:
            quiz_question_function(times_through, WORLD_QUESTIONS, quiz_question, WORLD_ANSWER_0, CAR_CORANSWER_0)
                
        elif quiz_question == 1:
            quiz_question_function(times_through, WORLD_QUESTIONS, quiz_question, WORLD_ANSWER_1, CAR_CORANSWER_1)
                
        elif quiz_question == 2:
            quiz_question_function(times_through, WORLD_QUESTIONS, quiz_question, WORLD_ANSWER_2, CAR_CORANSWER_2)
                    
        elif quiz_question == 3:
            quiz_question_function(times_through, WORLD_QUESTIONS, quiz_question, WORLD_ANSWER_3, CAR_CORANSWER_3)
                    
        elif quiz_question == 4:
            quiz_question_function(times_through, WORLD_QUESTIONS, quiz_question, WORLD_ANSWER_4, CAR_CORANSWER_4)
                    
        elif quiz_question == 5:
            quiz_question_function(times_through, WORLD_QUESTIONS, quiz_question, WORLD_ANSWER_5, CAR_CORANSWER_5)
            
        elif quiz_question == 6:
            quiz_question_function(times_through, WORLD_QUESTIONS, quiz_question, WORLD_ANSWER_6, CAR_CORANSWER_6)
                    
        elif quiz_question == 7:
            quiz_question_function(times_through, WORLD_QUESTIONS, quiz_question, WORLD_ANSWER_7, CAR_CORANSWER_7)
                    
        elif quiz_question == 8:
            quiz_question_function(times_through, WORLD_QUESTIONS, quiz_question, WORLD_ANSWER_8, CAR_CORANSWER_8)
            
        elif quiz_question == 9:
            quiz_question_function(times_through, WORLD_QUESTIONS, quiz_question, WORLD_ANSWER_9, CAR_CORANSWER_9)
            
        elif quiz_question == 10:
            quiz_question_function(times_through, WORLD_QUESTIONS, quiz_question, WORLD_ANSWER_10, CAR_CORANSWER_10)

        elif quiz_question == 11:
            quiz_question_function(times_through, WORLD_QUESTIONS, quiz_question, WORLD_ANSWER_11, CAR_CORANSWER_11)
                    
        elif quiz_question == 12:
            quiz_question_function(times_through, WORLD_QUESTIONS, quiz_question, WORLD_ANSWER_12, CAR_CORANSWER_12)
                    
        elif quiz_question == 13:
            quiz_question_function(times_through, WORLD_QUESTIONS, quiz_question, WORLD_ANSWER_13, CAR_CORANSWER_13)
                    
        elif quiz_question == 14:    
            quiz_question_function(times_through, WORLD_QUESTIONS, quiz_question, WORLD_ANSWER_14, CAR_CORANSWER_14)
            
        else:
            clear_screen()
            print("There has been an internal error, sorry ):")
            time.sleep(1)
            print("We will send you back to the main menu.")
            time.sleep(1)
            # menu()

    if corrects > times_through * 0.8:
        print("Well done {}!, You got {} out of {} Correct, thats {}% correct!".format(name, corrects, times_through, corrects / times_through * 100))
    
    elif corrects > times_through * 0.5:
        print("Nice job {}!, You got {} out of {} Correct, thats {}% correct!".format(name, corrects, times_through, corrects / times_through * 100))
    
    else:
        print("Nice try {}, You got out of {} Correct, thats {}% correct!, you'll do better next time!!".format(corrects, times_through, corrects / times_through * 100))
elif quiz_topic == "TECHNOLOGY":
    for questions in range(questions_per_round):
        quiz_question = random.randint(0, 14)
        times_through += 1
        while quiz_question in already_used:
            quiz_question = random.randint(0, 14)
            if quiz_question in already_used == False:
                break
        already_used.append(quiz_question)
        if quiz_question == 0:
            quiz_question_function(times_through, TECHNOLOGY_QUESTIONS, quiz_question, TECHNOLOGY_ANSWER_0, TECHNOLOGY_CORANSWER_0)
                
        elif quiz_question == 1:
            quiz_question_function(times_through, TECHNOLOGY_QUESTIONS, quiz_question, TECHNOLOGY_ANSWER_1, TECHNOLOGY_CORANSWER_1)
                
        elif quiz_question == 2:
            quiz_question_function(times_through, TECHNOLOGY_QUESTIONS, quiz_question, TECHNOLOGY_ANSWER_2, TECHNOLOGY_CORANSWER_2)
                    
        elif quiz_question == 3:
            quiz_question_function(times_through, TECHNOLOGY_QUESTIONS, quiz_question, TECHNOLOGY_ANSWER_3, TECHNOLOGY_CORANSWER_3)
                    
        elif quiz_question == 4:
            quiz_question_function(times_through, TECHNOLOGY_QUESTIONS, quiz_question, TECHNOLOGY_ANSWER_4, TECHNOLOGY_CORANSWER_4)
                    
        elif quiz_question == 5:
            quiz_question_function(times_through, TECHNOLOGY_QUESTIONS, quiz_question, TECHNOLOGY_ANSWER_5, TECHNOLOGY_CORANSWER_5)
            
        elif quiz_question == 6:
            quiz_question_function(times_through, TECHNOLOGY_QUESTIONS, quiz_question, TECHNOLOGY_ANSWER_6, TECHNOLOGY_CORANSWER_6)
                    
        elif quiz_question == 7:
            quiz_question_function(times_through, TECHNOLOGY_QUESTIONS, quiz_question, TECHNOLOGY_ANSWER_7, TECHNOLOGY_CORANSWER_7)
                    
        elif quiz_question == 8:
            quiz_question_function(times_through, TECHNOLOGY_QUESTIONS, quiz_question, TECHNOLOGY_ANSWER_8, TECHNOLOGY_CORANSWER_8)
            
        elif quiz_question == 9:
            quiz_question_function(times_through, TECHNOLOGY_QUESTIONS, quiz_question, TECHNOLOGY_ANSWER_9, TECHNOLOGY_CORANSWER_9)
            
        elif quiz_question == 10:
            quiz_question_function(times_through, TECHNOLOGY_QUESTIONS, quiz_question, TECHNOLOGY_ANSWER_10, TECHNOLOGY_CORANSWER_10)

        elif quiz_question == 11:
            quiz_question_function(times_through, TECHNOLOGY_QUESTIONS, quiz_question, TECHNOLOGY_ANSWER_11, TECHNOLOGY_CORANSWER_11)
                    
        elif quiz_question == 12:
            quiz_question_function(times_through, TECHNOLOGY_QUESTIONS, quiz_question, TECHNOLOGY_ANSWER_12, TECHNOLOGY_CORANSWER_12)
                    
        elif quiz_question == 13:
            quiz_question_function(times_through, TECHNOLOGY_QUESTIONS, quiz_question, TECHNOLOGY_ANSWER_13, TECHNOLOGY_CORANSWER_13)
                    
        elif quiz_question == 14:    
            quiz_question_function(times_through, TECHNOLOGY_QUESTIONS, quiz_question, TECHNOLOGY_ANSWER_14, TECHNOLOGY_CORANSWER_14)
            
        else:
            clear_screen()
            print("There has been an internal error, sorry ):")
            time.sleep(1)
            print("We will send you back to the main menu.")
            time.sleep(1)
            # menu()

    if corrects > times_through * 0.8:
        print("Well done {}!, You got {} out of {} Correct, thats {}% correct!".format(name, corrects, times_through, corrects / times_through * 100))
    
    elif corrects > times_through * 0.5:
        print("Nice job {}!, You got {} out of {} Correct, thats {}% correct!".format(name, corrects, times_through, corrects / times_through * 100))
    
    else:
        print("Nice try {}, You got out of {} Correct, thats {}% correct!, you'll do better next time!!".format(corrects, times_through, corrects / times_through * 100))
else: 
    print("You haven't chosen a topic, please choose a topic.")
    time.sleep(1)
    # choose_quiz_type()
