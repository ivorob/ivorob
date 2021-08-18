set nocompatible

filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin('~/.vim/bundle')

Plugin 'gmarik/Vundle.vim'

" git
Plugin 'airblade/vim-gitgutter'
" colors
Plugin 'NLKNguyen/papercolor-theme'

call vundle#end()

filetype plugin indent on

set tabstop=4
set expandtab
set shiftwidth=4
set noundofile
set nobackup

set cindent
syntax on
set background=dark
colorscheme PaperColor
set hlsearch

vmap <C-v> c<ESC>"+p
imap <C-v> <ESC>"+pa
