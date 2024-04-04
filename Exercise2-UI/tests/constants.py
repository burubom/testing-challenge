TIMEOUT = 200
RETRIES = 3
TARGET_URL = 'https://www.google.com/'
BASE_URL = 'https://www.debugbear.com/test/website-speed'
URL_INPUT_XPATH = '//*[@id="app"]/div/div[1]/form/div/input'
START_BTN_XPATH = '//*[@id="app"]/div/div[1]/form/div/button'
DEVICE_DROPDOWN_XPATH = '//*[@id="app"]/div/div[1]/div[1]/select'
SKIP_LINK_XPATH = '/html/body/div[9]/div/div/div/div/div[2]/a[2]'
TESTING_LABEL_XPATH = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]'
URL_TEXT_XPATH = '//*[@id="app"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[1]'
REGION_TEXT_XPATH = '//*[@id="app"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/span'
DEVICE_TEXT_XPATH = '//*[@id="app"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[3]/span'
SCORE_CLASS = 'scale-3'
LONG_URL = 'http://www.reallylong.link/rll/7MectGPZ5J3v/1FXcH55HKNpbb0GDvW26Xto0TcYugBuWENSVtDF_2lkSfqWOgxYpehD9uFPB_YCFRFUzUaUCrZzd7AROmFNqeLsD4mlF3N6i4lIjVRKtD/vurZzGMbfA7qUFBHQgeKH3dUmqOhs/HY0db5fe0m8Gt96cM2LrYGz3itgzwv9yururtovnxOXAMUJoClRXAB4SSJ20ibnraxn4WEkweDMaecT5v6Huy_I4heleSuov9NeSCCt5HO00DFcCGwBfZBWR4/tAiOPKGmv02QS7l4wZk6sZ9vxXnpGGeY2Qs2HwOTOnIlfW2FR9dWnzZENVHs_HFYXTUxeVEeORlAyTW5ISRO/AFGrlb6fNWD0CQC3dX2zhPoI2oIxiwoO1ZIf6eknLqyJ1UXOrP/D0UI/Qd6EPDh3VkQwim15fpdBT2WOXkSmrtmalyoJ3PK3rU80Pqr0Qcjm/I6mM0h/wKQO2p1vQgcxgLZPrEYiNxkwdPXH9ZiSphsxKNrUJhzRH/H7QKXBs7pU20SUr1jPAQuHvJfIvluA5D_CwSd5z5mi6Y4LU7sJ3felqEcF/ZXeReoUH_ZBr6X2qopwThRweNxPhy/Kl8mqZm3_TKyJaxmHA/n3RuIxaVaogZCYMS6ZRgy6PptqYX1J5WVgj/7hpVENDwKg7e7IqA5NmuSVBtdXts2KObiwDszyTlM5mlTzlmbASrHcFXLbDBs0fsxp7MGXUCZHmgP4D/a4bxK7jurmZ/fn35t20aS3DOtO1ItVBfWcmgKLdgD3GOsbhZ2iiBqAnD7m/dQjZ8P4/jUMABpwIoXY7LOuj27__IrpqIyjTvEFOhqzu6nJv3ZKIx4WNja0s/7bSDz1XO9/oKq_1hpYeuk/wPn2nYtdEw/Rmc4tDP9oiC4S8yQh2yssa6PbJPy0EFu8Rw/81KpNW3OuQJeyYQGZbzX4UM1OBfJv10zOe4YTZE4mw50PAt9hIkZgWxYxdGccyQ29dDQhU6QKPIizxvUzc0bUBlcACMzxI1rNxhV4dZ1g9RtxlAunl6IYAVeLaIlip_r3K9fN8becW2wntFhc6MJT8ur9hAP/6kSrihA8gz_h0S8wSad4KY/zuUN4dF3U0uF4qKwuOz9adgQ0CjaOBPQi2EkjJMLZCsKLUsqCa52g9z4t5wU6s_cGyfuRMyA_WLY8pmimGevMxSVn2pj1pbQQH5TpleePNH_O876U4hxUsFMU8SM3ir3dvkiPlnuGepOPS8E2ONIMYT9WQc9yB_mNNx_wGh_gZWBbV1E1bVqn1CJC79X9zSued1NQabJva27RKZu8YqRVgLZiOLlBq1PI38k0gGsZLjIQCjWjE84n5jz8m_tsSmQyVvp1n8pzUp3aMlofGEqWH8X5rSwHaOsdU5_REDFEv3I6zPVaOV0UpnpK5iXPp4FMtItohXHqJeS7rq0rNEakqNBDtMrgKz9XTnoWBEU9oO4USoLof8CDk_0lL_HlnY6gX68EtbOAhTRQJHxHYIqC9o_R1IN0mpzhkHSN1yPLBklUC0RO_B/a0ng/pBTJtwRPhNjcdyQn8bfxtbQ/42KfE5TXNOEzJ/2mlmTlpNsASBYkacfoK6b3XAhMkHhEOSwtM2r_F4c15LBqr7wpDNSB3HDbuYB8/T6HJ_is2bwvrv1L6QDeZWlhTt7r_AF1kDt9qIR8TbanWxIvAnw0IIopt6u1VUqp7KahJCm7Kg4ZDDHElahdntZFyVg_BoAB67XM33jxu4SozpZqLMqf84kO5jOMQ5s2LOQWILInIXlt2LHxwds1qnHf9RdFxRUeU0GXU3zG5VxkuwpjMpkxC_G2d5yKHWmQCFlnnSg4b_POjBG6m4bk0WFLWhiKcxE_MI0_wPzL65_d2RLFbnI2Fanli/SHlW5ODpTgkfXnBkjpZ4PMJrN/3JmW9i87N4dW5Z8C1rj0w5bldtWBEBTrKSQSbIGxx'
METRICS = {
    'Overview': [
        'Full TTFB',
        'First Contentful Paint',
        'Largest Contentful Paint',
        'Speed Index',
        'CPU Time',
        'Total Blocking Time',
        'Cumulative Layout Shift',
        'Page Weight'
    ],
    'Web Vitals': [
        'First Contentful Paint (CrUX) — URL',
        'Largest Contentful Paint (CrUX) — URL',
        'Cumulative Layout Shift (CrUX) — URL',
        'Interaction to Next Paint (CrUX) — URL',
        'First Contentful Paint',
        'Largest Contentful Paint',
        'Cumulative Layout Shift',
        'Total Blocking Time',
        'First Input Delay (CrUX) — URL',
        'Time to First Byte (CrUX) — URL',
        'Good (CrUX)',
        'Full TTFB'
    ],
    'Requests': [
        'Request Waterfall',
        'Third Parties'
    ],
    'Lighthouse': [
        'Performance',
        'Accessibility',
        'Best Practices',
        'SEO'
    ]
}
