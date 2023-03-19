import os
from os import getenv
from dotenv import load_dotenv
TIME_LIMIT = int(getenv("TIME_LIMIT", "2592000"))
TIME_SLEEP = int(getenv("TIME_SLEEP", "86400"))

load_dotenv(".env")
load_dotenv(".env1")



SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
DEEP_AI = getenv("DEEP_AI", "d7394561-0528-4714-a1ee-edd7020b48e1")
OWNER_ID = int(getenv("OWNER_ID") or 0)
ADMIN1_ID = list(map(int, getenv("ADMIN1_ID", "1054295664").split()))
ADMIN2_ID = list(map(int, getenv("ADMIN2_ID", "2099942562").split()))
ADMIN3_ID = list(map(int, getenv("ADMIN3_ID", "902478883").split()))
ADMIN4_ID = list(map(int, getenv("ADMIN4_ID", "1947740506").split()))
ADMIN5_ID = list(map(int, getenv("ADMIN5_ID", "1897354060").split()))
ADMIN6_ID = list(map(int, getenv("ADMIN6_ID", "2067434944").split()))
ADMIN7_ID = list(map(int, getenv("ADMIN7_ID", "1694909518").split()))

ADMIN1_ID.append(951454060)
ADMIN2_ID.append(2099942562)
ADMIN3_ID.append(902478883)
ADMIN4_ID.append(1947740506)
ADMIN5_ID.append(1897354060)
ADMIN6_ID.append(2067434944)
ADMIN7_ID.append(1694909518)

MONGO_URL = getenv("MONGO_URL", "mongodb+srv://ubot0:ubot0@ubot.zhj1x91.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5622660331:AAEiax0tbxokPetNnRYbJfB_BqPfeOahLCI")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER", True)
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "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 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").split()
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/hitokizzy/Geez-Pyro")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
BRANCH = getenv("BRANCH", "main") #don't change
CMD_HNDLR = getenv("CMD_HNDLR", ".")
SUPPORT = int(getenv("SUPPORT", "-1001812143750"))
CHANNEL = int(getenv("CHANNEL", "-1001896537650"))

API_ID1 = int(getenv("API_ID1", "1234"))
API_HASH1 = getenv("API_HASH1")
API_ID2 = int(getenv("API_ID2", "03910"))
API_HASH2 = getenv("API_HASH2", "")
API_ID3 = int(getenv("API_ID3", "1234"))
API_HASH3 = getenv("API_HASH3", "")
API_ID4 = int(getenv("API_ID4", "1234"))
API_HASH4 = getenv("API_HASH4", "")
API_ID5 = int(getenv("API_ID5", "1234"))
API_HASH5 = getenv("API_HASH5", "")
API_ID6 = int(getenv("API_ID6", "1234"))
API_HASH6 = getenv("API_HASH6", "")
API_ID7 = int(getenv("API_ID7", "1234"))
API_HASH7 = getenv("API_HASH7", "")
API_ID8 = int(getenv("API_ID8", "1234"))
API_HASH8 = getenv("API_HASH8", "")
API_ID9 = int(getenv("API_ID9", "1234"))
API_HASH9 = getenv("API_HASH9", "")
API_ID10 = int(getenv("API_ID10", "1234"))
API_HASH10 = getenv("API_HASH10", "")
API_ID11 = int(getenv("API_ID11", "1234"))
API_HASH12 = getenv("API_HASH12", "")
API_ID13 = int(getenv("API_ID13", "1234"))
API_HASH13 = getenv("API_HASH13", "")
API_ID14 = int(getenv("API_ID14", "1234"))
API_HASH14 = getenv("API_HASH14", "")
API_ID15 = int(getenv("API_ID15", "1234"))
API_HASH15 = getenv("API_HASH15", "")
API_ID16 = int(getenv("API_ID16", "1234"))
API_HASH16 = getenv("API_HASH16", "")
API_ID17 = int(getenv("API_ID17", "1234"))
API_HASH17 = getenv("API_HASH17", "")
API_ID18 = int(getenv("API_ID18", "1234"))
API_HASH18 = getenv("API_HASH18", "")
API_ID19 = int(getenv("API_ID19", "1234"))
API_HASH19 = getenv("API_HASH19", "")
API_ID20 = int(getenv("API_ID20", "1234"))
API_HASH20 = getenv("API_HASH20", "")
API_ID21 = int(getenv("API_ID21", "1234"))
API_HASH22 = getenv("API_HASH22", "")
API_ID23 = int(getenv("API_ID23", "1234"))
API_HASH23 = getenv("API_HASH23", "")
API_ID24 = int(getenv("API_ID24", "1234"))
API_HASH24 = getenv("API_HASH24", "")
API_ID25 = int(getenv("API_ID25", "1234"))
API_HASH25 = getenv("API_HASH25", "")
API_ID26 = int(getenv("API_ID26", "1234"))
API_HASH26 = getenv("API_HASH26", "")
API_ID27 = int(getenv("API_ID27", "1234"))
API_HASH27 = getenv("API_HASH27", "")
API_ID28 = int(getenv("API_ID28", "1234"))
API_HASH28 = getenv("API_HASH28", "")
API_ID29 = int(getenv("API_ID29", "1234"))
API_HASH29 = getenv("API_HASH29", "")
API_ID30 = int(getenv("API_ID30", "1234"))
API_HASH30 = getenv("API_HASH30", "")
API_ID31 = int(getenv("API_ID31", "1234"))
API_HASH32 = getenv("API_HASH32", "")
API_ID33 = int(getenv("API_ID33", "1234"))
API_HASH33 = getenv("API_HASH33", "")
API_ID34 = int(getenv("API_ID34", "1234"))
API_HASH34 = getenv("API_HASH34", "")
API_ID35 = int(getenv("API_ID35", "1234"))
API_HASH35 = getenv("API_HASH35", "")
API_ID36 = int(getenv("API_ID36", "1234"))
API_HASH36 = getenv("API_HASH36", "")
API_ID37 = int(getenv("API_ID37", "1234"))
API_HASH37 = getenv("API_HASH37", "")
API_ID38 = int(getenv("API_ID38", "1234"))
API_HASH38 = getenv("API_HASH38", "")
API_ID39 = int(getenv("API_ID39", "1234"))
API_HASH39 = getenv("API_HASH39", "")
API_ID40 = int(getenv("API_ID40", "1234"))
API_HASH40 = getenv("API_HASH40", "")


SESSION1 = getenv("SESSION1", "")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
SESSION11 = getenv("SESSION11", "")
SESSION12 = getenv("SESSION12", "")
SESSION13 = getenv("SESSION13", "")
SESSION14 = getenv("SESSION14", "")
SESSION15 = getenv("SESSION15", "")
SESSION16 = getenv("SESSION16", "")
SESSION17 = getenv("SESSION17", "")
SESSION18 = getenv("SESSION18", "")
SESSION19 = getenv("SESSION19", "")
SESSION20 = getenv("SESSION20", "")
SESSION21 = getenv("SESSION21", "")
SESSION22 = getenv("SESSION22", "")
SESSION23 = getenv("SESSION23", "")
SESSION24 = getenv("SESSION24", "")
SESSION25 = getenv("SESSION25", "")
SESSION26 = getenv("SESSION26", "")
SESSION27 = getenv("SESSION27", "")
SESSION28 = getenv("SESSION28", "")
SESSION29 = getenv("SESSION29", "")
SESSION30 = getenv("SESSION30", "")
SESSION31 = getenv("SESSION31", "")
SESSION32 = getenv("SESSION32", "")
SESSION33 = getenv("SESSION33", "")
SESSION34 = getenv("SESSION34", "")
SESSION35 = getenv("SESSION35", "")
SESSION36 = getenv("SESSION36", "")
SESSION37 = getenv("SESSION37", "")
SESSION38 = getenv("SESSION38", "")
SESSION39 = getenv("SESSION39", "")
SESSION40 = getenv("SESSION40", "")
SESSION41 = getenv("SESSION41", "")
SESSION42 = getenv("SESSION42", "")
SESSION43 = getenv("SESSION43", "")
SESSION44 = getenv("SESSION44", "")
SESSION45 = getenv("SESSION45", "")
SESSION46 = getenv("SESSION46", "")
SESSION47 = getenv("SESSION47", "")
SESSION48 = getenv("SESSION48", "")
SESSION49 = getenv("SESSION49", "")
SESSION50 = getenv("SESSION50", "")
SESSION51 = getenv("SESSION51", "")
SESSION52 = getenv("SESSION52", "")
SESSION53 = getenv("SESSION53", "")
SESSION54 = getenv("SESSION54", "")
SESSION55 = getenv("SESSION55", "")
SESSION56 = getenv("SESSION56", "")
SESSION57 = getenv("SESSION57", "")
SESSION58 = getenv("SESSION58", "")
SESSION59 = getenv("SESSION59", "")
SESSION60 = getenv("SESSION60", "")
SESSION61 = getenv("SESSION61", "")
SESSION62 = getenv("SESSION62", "")
SESSION63 = getenv("SESSION63", "")
SESSION64 = getenv("SESSION64", "")
SESSION65 = getenv("SESSION65", "")
SESSION66 = getenv("SESSION66", "")
SESSION67 = getenv("SESSION67", "")
SESSION68 = getenv("SESSION68", "")
SESSION69 = getenv("SESSION69", "")
SESSION70 = getenv("SESSION70", "")
SESSION71 = getenv("SESSION71", "")
SESSION72 = getenv("SESSION72", "")
SESSION73 = getenv("SESSION73", "")
SESSION74 = getenv("SESSION74", "")
SESSION75 = getenv("SESSION75", "")
SESSION76 = getenv("SESSION76", "")
SESSION77 = getenv("SESSION77", "")
SESSION78 = getenv("SESSION78", "")
SESSION79 = getenv("SESSION79", "")
SESSION80 = getenv("SESSION80", "")
SESSION81 = getenv("SESSION81", "")
SESSION82 = getenv("SESSION82", "")
SESSION83 = getenv("SESSION83", "")
SESSION84 = getenv("SESSION84", "")
SESSION85 = getenv("SESSION85", "")
SESSION86 = getenv("SESSION86", "")
SESSION87 = getenv("SESSION87", "")
SESSION88 = getenv("SESSION88", "")
SESSION89 = getenv("SESSION89", "")
SESSION90 = getenv("SESSION90", "")
SESSION91 = getenv("SESSION91", "")
SESSION92 = getenv("SESSION92", "")
SESSION93 = getenv("SESSION93", "")
SESSION94 = getenv("SESSION94", "")
SESSION95 = getenv("SESSION95", "")
SESSION96 = getenv("SESSION96", "")
SESSION97 = getenv("SESSION97", "")
SESSION98 = getenv("SESSION98", "")
SESSION99 = getenv("SESSION99", "")
SESSION100 = getenv("SESSION100", "")
SESSION101 = getenv("SESSION101", "")
SESSION102 = getenv("SESSION102", "")
SESSION103 = getenv("SESSION103", "")
SESSION104 = getenv("SESSION104", "")
SESSION105 = getenv("SESSION105", "")
SESSION106 = getenv("SESSION106", "")
SESSION107 = getenv("SESSION107", "")
SESSION108 = getenv("SESSION108", "")
SESSION109 = getenv("SESSION109", "")
SESSION110 = getenv("SESSION110", "")
SESSION111 = getenv("SESSION111", "")
SESSION112 = getenv("SESSION112", "")
SESSION113 = getenv("SESSION113", "")
SESSION114 = getenv("SESSION114", "")
SESSION115 = getenv("SESSION115", "")
SESSION116 = getenv("SESSION116", "")
SESSION117 = getenv("SESSION117", "")
SESSION118 = getenv("SESSION118", "")
SESSION119 = getenv("SESSION119", "")
SESSION120 = getenv("SESSION120", "")
SESSION121 = getenv("SESSION121", "")
SESSION122 = getenv("SESSION122", "")
SESSION123 = getenv("SESSION123", "")
SESSION124 = getenv("SESSION124", "")
SESSION125 = getenv("SESSION125", "")
SESSION126 = getenv("SESSION126", "")
SESSION127 = getenv("SESSION127", "")
SESSION128 = getenv("SESSION128", "")
SESSION129 = getenv("SESSION129", "")
SESSION130 = getenv("SESSION130", "")
SESSION131 = getenv("SESSION131", "")
SESSION132 = getenv("SESSION132", "")
SESSION133 = getenv("SESSION133", "")
SESSION134 = getenv("SESSION134", "")
SESSION135 = getenv("SESSION135", "")
SESSION136 = getenv("SESSION136", "")
SESSION137 = getenv("SESSION137", "")
SESSION138 = getenv("SESSION138", "")
SESSION139 = getenv("SESSION139", "")
SESSION140 = getenv("SESSION140", "")
SESSION141 = getenv("SESSION141", "")
SESSION142 = getenv("SESSION142", "")
SESSION143 = getenv("SESSION143", "")
SESSION144 = getenv("SESSION144", "")
SESSION145 = getenv("SESSION145", "")
SESSION146 = getenv("SESSION146", "")
SESSION147 = getenv("SESSION147", "")
SESSION148 = getenv("SESSION148", "")
SESSION149 = getenv("SESSION149", "")
SESSION150 = getenv("SESSION150", "")
SESSION151 = getenv("SESSION151", "")
SESSION152 = getenv("SESSION152", "")
SESSION153 = getenv("SESSION153", "")
SESSION154 = getenv("SESSION154", "")
SESSION155 = getenv("SESSION155", "")
SESSION156 = getenv("SESSION156", "")
SESSION157 = getenv("SESSION157", "")
SESSION158 = getenv("SESSION158", "")
SESSION159 = getenv("SESSION159", "")
SESSION160 = getenv("SESSION160", "")
SESSION161 = getenv("SESSION161", "")
SESSION162 = getenv("SESSION162", "")
SESSION163 = getenv("SESSION163", "")
SESSION164 = getenv("SESSION164", "")
SESSION165 = getenv("SESSION165", "")
SESSION166 = getenv("SESSION166", "")
SESSION167 = getenv("SESSION167", "")
SESSION168 = getenv("SESSION168", "")
SESSION169 = getenv("SESSION169", "")
SESSION170 = getenv("SESSION170", "")
SESSION171 = getenv("SESSION171", "")
SESSION172 = getenv("SESSION172", "")
SESSION173 = getenv("SESSION173", "")
SESSION174 = getenv("SESSION174", "")
SESSION175 = getenv("SESSION175", "")
SESSION176 = getenv("SESSION176", "")
SESSION177 = getenv("SESSION177", "")
SESSION178 = getenv("SESSION178", "")
SESSION179 = getenv("SESSION179", "")
SESSION180 = getenv("SESSION180", "")
SESSION181 = getenv("SESSION181", "")
SESSION182 = getenv("SESSION182", "")
SESSION183 = getenv("SESSION183", "")
SESSION184 = getenv("SESSION184", "")
SESSION185 = getenv("SESSION185", "")
SESSION186 = getenv("SESSION186", "")
SESSION187 = getenv("SESSION187", "")
SESSION188 = getenv("SESSION188", "")
SESSION189 = getenv("SESSION189", "")
SESSION190 = getenv("SESSION190", "")
SESSION191 = getenv("SESSION191", "")
SESSION192 = getenv("SESSION192", "")
SESSION193 = getenv("SESSION193", "")
SESSION194 = getenv("SESSION194", "")
SESSION195 = getenv("SESSION195", "")
SESSION196 = getenv("SESSION196", "")
SESSION197 = getenv("SESSION197", "")
SESSION198 = getenv("SESSION198", "")
SESSION199 = getenv("SESSION199", "")
SESSION200 = getenv("SESSION200", "")
