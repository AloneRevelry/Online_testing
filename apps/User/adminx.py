import xadmin
from xadmin import views

class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True


class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "上机考试系统后台管理"  # 设置站点标题
    site_footer = "https://github.com/AloneRevelry/Online_testing"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠


xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)