set nocompatible

filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin('~/.vim/bundle')

Plugin 'gmarik/Vundle.vim'

" git
Plugin 'airblade/vim-gitgutter'
" colors
Plugin 'NLKNguyen/papercolor-theme'
" clang-format
Plugin 'rhysd/vim-clang-format'

call vundle#end()

filetype plugin indent on

set backspace=indent,eol,start

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
