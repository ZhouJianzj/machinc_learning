# pyecharts的使用 参见:官网文档 https://gallery.pyecharts.org/#/Pie/pie_set_color
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
areas = ['南京', '扬州', '天津', '上海']
values = [100,23,45,67]
print([list(z) for z in zip(areas, areas)])

c = (
    Pie()
        .add("", [list(z) for z in zip(areas, values)])
        .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
        .set_global_opts(title_opts=opts.TitleOpts(title="地区分布"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        .render("pie_set_color.html")
)
