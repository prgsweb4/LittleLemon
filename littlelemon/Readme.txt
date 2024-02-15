admin/
api/
restaurant/

users/
users/ ^tables/$ [name='booking-list']
users/ ^tables\.(?P<format>[a-z0-9]+)/?$ [name='booking-list']
users/ ^tables/(?P<pk>[^/.]+)/$ [name='booking-detail']
users/ ^tables/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='booking-detail']
users/ ^users/$ [name='user-list']
users/ ^users\.(?P<format>[a-z0-9]+)/?$ [name='user-list']
users/ ^users/(?P<pk>[^/.]+)/$ [name='user-detail']
users/ ^users/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='user-detail']
users/ ^$ [name='api-root']
users/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']

booking/
booking/ ^tables/$ [name='booking-list']
booking/ ^tables\.(?P<format>[a-z0-9]+)/?$ [name='booking-list']
booking/ ^tables/(?P<pk>[^/.]+)/$ [name='booking-detail']
booking/ ^tables/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='booking-detail']
booking/ ^users/$ [name='user-list']
booking/ ^users\.(?P<format>[a-z0-9]+)/?$ [name='user-list']
booking/ ^users/(?P<pk>[^/.]+)/$ [name='user-detail']
booking/ ^users/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='user-detail']
booking/ ^$ [name='api-root']
booking/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']

api-auth/
auth/

auth/ ^users/$ [name='user-list']
auth/ ^users\.(?P<format>[a-z0-9]+)/?$ [name='user-list']
auth/ ^users/activation/$ [name='user-activation']
auth/ ^users/activation\.(?P<format>[a-z0-9]+)/?$ [name='user-activation']
auth/ ^users/me/$ [name='user-me']
auth/ ^users/me\.(?P<format>[a-z0-9]+)/?$ [name='user-me']
auth/ ^users/resend_activation/$ [name='user-resend-activation']
auth/ ^users/resend_activation\.(?P<format>[a-z0-9]+)/?$ [name='user-resend-activation']
auth/ ^users/reset_password/$ [name='user-reset-password']
auth/ ^users/reset_password\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-password']
auth/ ^users/reset_password_confirm/$ [name='user-reset-password-confirm']
auth/ ^users/reset_password_confirm\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-password-confirm']
auth/ ^users/reset_username/$ [name='user-reset-username']
auth/ ^users/reset_username\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-username']
auth/ ^users/reset_username_confirm/$ [name='user-reset-username-confirm']
auth/ ^users/reset_username_confirm\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-username-confirm']
auth/ ^users/set_password/$ [name='user-set-password']
auth/ ^users/set_password\.(?P<format>[a-z0-9]+)/?$ [name='user-set-password']
auth/ ^users/set_username/$ [name='user-set-username']
auth/ ^users/set_username\.(?P<format>[a-z0-9]+)/?$ [name='user-set-username']
auth/ ^users/(?P<id>[^/.]+)/$ [name='user-detail']
auth/ ^users/(?P<id>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='user-detail']
auth/ ^$ [name='api-root']
auth/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
auth/ ^token/login/?$ [name='login']
auth/ ^token/logout/?$ [name='logout']
