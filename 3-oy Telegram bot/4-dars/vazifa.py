import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

BOT_TOKEN = "7615889631:AAHMhlpRiv8YnFDbctE9aC_-ka5yg_V7nSU"  # <-- bu yerga tokeningizni yozing

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


btn1 = KeyboardButton(text="Moshina 🚗")
btn2 = KeyboardButton(text="Tabiat 🏞️")
btn3 = KeyboardButton(text="O'zim haqimda 🤷‍♂️")
btn4 = KeyboardButton(text="Yordam 👍")
btn5 = KeyboardButton(text="Dars 📋")

kb = ReplyKeyboardMarkup(
    keyboard=[
        [btn1, btn2],
        [btn3, btn4, btn5]
    ],
    resize_keyboard=True
)


@dp.message(Command("start"))
async def start_hand(message: types.Message):
    await message.answer("Tugmalardan birini tanlang", reply_markup=kb)


@dp.message()
async def answer(message: types.Message):
    if message.text == "Moshina 🚗":
        await message.answer(
            "BMW Group premium avtomobillar va mototsikllarni yetkazib berish bo‘yicha"
            " dunyodagi yetakchi provayder bo‘lib, BMW, MINI, Rolls-Royce va BMW "
            "Motorrad brendlarining uyidir. Bizning transport vositalarimiz "
            "va mahsulotlarimiz mijozlarimizning ehtiyojlariga moslashtirilgan"
            " va doimiy ravishda takomillashtiriladi - barqarorlik va resurslarni "
            "tejashga aniq e'tibor qaratiladi.")

    elif message.text == "Tabiat 🏞️":
        await message.answer("Tabiat — odamning paydo boʻlgunicha ham, odam ishtiroki bilan ham mavjud borliq. Umuman — bu dunyo, odam, koinot; mikromakromega dunyolar; Jonsiz. va jonli narsalar bor. Tor maʼnoda — tabiat fanlari oʻrganadigan obyekt. Tabiat odamga, jamiyatga bogʻliq boʻlmagan qonuniyatga boʻysunadi. Odam tabiatning bir qismi. Odam tabiat qonunlarini oʻzgartira olmaydi, faqat qonunlardan foydalanib, tabiat elementlarini, qismlarini oʻzlashtirishi mumkin. Tabiat tushunchasi insoniyat jamiyati yashashi tabiiy sharoitlarining majmui sifatida ham qaraladi. Inson yashashi uchun mehnat qiladi, mehnat (mas., dehqonchilik, qurilish, sanoat), miya faoliyati va boshqa esa tabiatning baʼzi jihatlarini oʻzgartiradi. Odam tomonidan, yaʼni ijtimoiy mehnat jarayonida yaratiladigan moddiy boyliklar shartli ravishda „ikkinchi tabiat“ deyiladi. Masalan, vodoroddan urangacha boʻlgan 92 ta kimyoviy element"
                             " tabiiydir, undan keyingi kashf etilganlari sunʼiydir. Barcha sunʼiy sintetik kimyoviy birikmalar, odam yaratayotgan atom va yadro energiyalari „ikkinchi tabiat“ga kiradi.")

    elif message.text == "O'zim haqimda 🤷‍♂️":
        await message.answer("men judaham odobli va Alochiman "
                             "ukam ham ITda faol ")
    elif message.text == "Yordam 👍":
        await message.answer("Sizga nimadirnidir bilmasangiz sizga CHAT GPT yordam beroladi")

    elif message.text == "Dars 📋":
        await message.answer("Dars – maktab taʼlimining asosiy tashkiliy shakli. Dars muayyan miqdordagi doimiy oʻquvchilar tarkibi bilan qatʼiy tartibda uyushtiriladigan va aniq maqsadga yoʻnaltirilgan didaktik tadbirdir. Dars – insoniyat tomonidan minglab yillar mobaynida orttirilgan hayotiy tajribalarni oʻquvchilarga juda qisqa vaqtda oʻrgatishning eng samarali usuli. Taʼlimning dars shakli Turkistonda uzoq zamonlardan buyon qoʻllanilib kelgan. Darsni tashkil etish va uning samaradorligini taʼminlashda oʻqituvchining oʻrni beqiyos boʻlgan. Turkiston maktablarida taʼlimning tashqi shakliy jihatlariga emas, balki mohiyatiga ham eʼtibor berilgan. Chunonchi, oʻquvchilarning tayyorligini aniqlash, ularni guruhlarga ajratishda bolalarning yoshi va maktabda qancha vaqt oʻqiganligiga emas, balki oʻtilgan mashgʻulotlarni nechogʻli oʻzlashtirganliklariga tayanilgan. Turkiston maktablarida taʼlimning dars shakli boʻlganligi bilan mashgʻulotlarni sinfdars tizimi tarzida uyushtirish tajribasi boʻlmagan. Shuningdek, darsning davomiyligi, predmetlarning oʻrinlashuvi, kundalik mashgulotlarning miqdori singari taʼlimiy chegaralar har bir oʻqituvchining uzi tomonidan belgilangan. Dars kadars turkiy maorif tizimida oliy va oʻrta taʼlim boʻgʻinlarini ifoda etgan Madrasa taʼlimida ham asosiy ish shakli hisoblangan. Madrasalarda dars belgilangan muayyan tartib asosida uyushtirilgan. Ayni vaqtda, Madrasa darslarida talabalarning mustaqil oʻzlash-tirishlariga katta eʼtibor qaratilgan. Qadars taʼlim muassasalari uchun darsning jamoa va individual shakllari krri-shikligi xos boʻlgan."

"Dars taʼlimning jamoa boʻlib amalga oshirilish tarzi sifatida ijtimoiy ahamiyat kasb etadi. Shuningdek, dars maktab yoshidagi bolalarni yalpi oʻqitishni osonlashtiradi, ularni jamoa sifatida tarbiyalashga hissa qoʻshadi, bolalarda ijtimoiy faollik va muomala madaniyatining shakllanishiga koʻmaklashadi. Darsda oʻquv mashgʻulotlarining individual, guruhiy va umumsinf shakllari uygʻunlashadi."

"Har qanday jamiyatda dars jamiyat tomonidan taʼlim oldiga qoʻyilgan vazifalarni bajarish uchun xizmat qiladi. Darsning vazifalari taʼlim jarayonining qonuniyatlari va muayyan jamiyatning komil shaxs borasidagi tushunchalari bilan qatʼiylashadi."

"Yangilanayotgan pedagogik tafakkur talablariga koʻra zamonaviy dars oʻquv muassasasining mulkiy mansubligidan qatʼi nazar quyidagi xususiyatlarga ega boʻlishi lozim: taʼlimning tarbiyaviy maqsadlarga boʻysundirilganligi, oʻquvchini komil shaxs sifatida shakllantirishga yoʻnaltirilganligi, ilmiyligi va izchilligi, tarbiyalanuvchining faolligi va mustaqilligini taʼminlashga qaratilganligi, insonparvarlik yoʻnalishiga egaligi, tizimliligi, bilimlarni ongli ravishda oʻzlashtirishga qaratilganligi, amaliy axa-miyatga egaligi va hokazo."

"Zamonaviy taʼlim tajribasida bir dars uchun belgilangan standart vaqt mavjudars Bu vaqt taʼlim muassasalarining tabiati, taʼlimning bosqichlari va oʻquvchilar imkoniyatidan kelib chiqib, 45, 40, 35 va 30 min.ni tashkil etadi."

"Taʼlim tizimida dars va uy vazifasi munosabatlari oʻta muhim sanaladi. Zamonaviy taʼlim tizimining turli bosqichlarida oʻquvchilarga uy vazifasi berilishi yoki berilmasligi, uning miqdori singari jiqatlar oʻquv muassasalarining nizomlarida aks ettiriladi."

"Pedars fani va amaliyoti uchun darsning tarkibi masalasi ham muammoli. Uzoq vaqt davomida har bir dars yangi mavzuning bayoni, uni oʻquvchi xotirasida mustaqkamlash, bilimlarni amaliyotda qoʻllash kabi qismlardan iborat boʻlishi shart deb hisoblab kelingan. Oʻquv jarayoni mantiqan bunday katʼ-iy tarkibni talab etmaydi. Dars va maktab tajribasi bu tizimni maʼqullamadi. Oʻquv jarayonida darsni tashkil etishning oldindan belgilab qoʻyil-magan va hamma uchun majburiy boʻlmagan har xil yoʻllarini qoʻllash maqsadga muvofiqdir. Olingan bilimlarni amaliyotda qoʻllash hamisha mavzuni mustahkamlashning manbai boʻlib kelgan va bu masalani dars tarkibida alohida koʻrsatishning hojati ham yoʻq. Bir necha darsni yangi mavzuning bayoniga bagʻishlash, ayrimlarini lab. topshiriklarini bajarishga ajratish ham mumkin. Muhimi, oʻtilayotgan mavzu oʻquvchilar tomonidan oʻzlashtirilib, ularda koʻnikma paydo boʻlishi va bu koʻnikmalarni amaliyotda qoʻllab malakaga aylantira bilishlaridir."

"Dars tarkibi masalasi darsni tasniflash, yaʼni tipologiya bilan bogʻliq. Pedagogik adabiyotlarda dars mazmunga, didaktik maqsadga, oʻtish yoʻllariga, taʼlim jarayonining xususiyatlari va uning qismlariga koʻra tasnif qilingan. Odatda, dars kirish, yangi bilim berish, mustahkamlash, koʻnikma va malakalarni shakllantirish, bilimlarni amaliyotda qoʻllash, nazorat qilish va aralash kabi turlarga boʻlinadi. Taʼlim tajribasida bir dars jarayonida bir yoki bir necha dars turlari umumlashtirilgan holda ish olib boriladigan aralash dars koʻp uchraydi. Dars oʻquv jarayonining yol-gʻiz shakli emas. Turli sinflarda fakultativ mashgʻulotlar, seminar, oʻquv konferensiyalari, bahslar, muammoli darslar, amaliy ishlar, ustaxonada ishlash kabi darslar mavjudars")


async def main():
    print("Bugungi darsgi bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


