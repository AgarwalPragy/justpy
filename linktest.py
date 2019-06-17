import justpy as jp

def click_me(self, msg):
    print(msg)

def link_test(request):
    wp = jp.WebPage()
    h = jp.Hello(a=wp)
    l = jp.LinkJP(text='my link', a=wp, classes='text-red-500 text-2xl')
    d = []
    for i in range(100):
        d.append(jp.Div(text=f'{i}) Div', classes=h.classes, a=wp))
    l.bookmark = d[30]
    l.scroll = True
    # l.on('click', click_me)
    return wp


jp.justpy(link_test)