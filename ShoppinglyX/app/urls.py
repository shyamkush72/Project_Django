from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, PasscodeChange, PassCodeReset, MysetPassword
urlpatterns = [
    # path('', views.home),
    path("",views.ProductView.as_view(),name='home'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('ShowCart/', views.ShowCart, name='showcart'),
    path('pluscart/',views.PlusCart,name='pluscart'),
    path('minuscart/',views.MinusCart,name='minuscart'),
    path('removecart/',views.RemoveCart,name='removecart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobiledata/<slug:data>', views.mobile, name='mobiledata'),
    path('laptop/',views.laptop,name='laptop'),
    path('laptopdata/<slug:data>',views.laptop,name='laptopdata'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name="app/login.html",authentication_form=LoginForm),name='login'),
    path('logout/',auth_view.LogoutView.as_view(next_page="login"),name="logout"),
    path('topwear/', views.topwear, name='topwear'),
    path('topwear/<slug:data>', views.topwear, name='topweardata'),
    path('bottomwear/', views.bottomwear, name='bottomwear'),
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name="app/passwordReset.html",form_class=PassCodeReset),name='password_reset'),
    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name="app/passwordResetDone.html"),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name="app/passwordResetConfirm.html",form_class=MysetPassword),name='password_reset_confirm'),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name="app/passwordResetComplete.html"),name='password_reset_complete'),
    path('bottomwear/<slug:data>', views.bottomwear, name='bottomweardata'),
    path('registration/', views.UserCreationView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('change_password/', auth_view.PasswordChangeView.as_view(template_name="app/passwordChange.html",form_class=PasscodeChange,success_url='/logout/'), name='PasswordChange'),
    ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
