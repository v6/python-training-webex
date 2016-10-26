package { 'tree':
  ensure => 'installed',
}

package { 'epel-release':
  ensure => 'installed',
}

package { 'python34': 
  ensure => 'installed',
}

package { 'vim':
  ensure => 'installed',
}

package { 'git':
  ensure => 'installed',
}
