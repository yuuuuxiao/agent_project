import request from '@/utils/request'

/** 获取当前用户信息 */
export function getUserInfoApi() {
  return request({
    url: '/api/user/me',
    method: 'get'
  })
}

/** 修改个人信息 */
export function updateUserInfoApi(data) {
  return request({
    url: '/api/user/me',
    method: 'put',
    data
  })
}
