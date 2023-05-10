all:
	$(MAKE) -C echo2vgm
	$(MAKE) -C eif2tfi/tool
	$(MAKE) -C headgen/tool
	$(MAKE) -C mdtiler/tool
	$(MAKE) -C midi2esf
	$(MAKE) -C mml2esf/tool
	$(MAKE) -C pcm2ewf/tool
	$(MAKE) -C romfix
	$(MAKE) -C slz/tool
	$(MAKE) -C tfi2eif/tool
	$(MAKE) -C uftc/tool
	$(MAKE) -C vgi2eif/tool

clean:
	$(MAKE) clean -C echo2vgm
	$(MAKE) clean -C eif2tfi/tool
	$(MAKE) clean -C headgen/tool
	$(MAKE) clean -C mdtiler/tool
	$(MAKE) clean -C midi2esf
	$(MAKE) clean -C mml2esf/tool
	$(MAKE) clean -C pcm2ewf/tool
	$(MAKE) clean -C romfix
	$(MAKE) clean -C slz/tool
	$(MAKE) clean -C tfi2eif/tool
	$(MAKE) clean -C uftc/tool
	$(MAKE) clean -C vgi2eif/tool