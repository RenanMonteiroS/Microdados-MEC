def abre_arquivo():
    dict_info = {'2008': '', '2009': '', '2010': '', '2011': '', '2012': ''}
    arquivos = {'enade_2008': 'microdados/microdados_enade_2008.csv',
                'enade_2009': 'microdados/microdados_enade_2009.csv',
                'enade_2010': 'microdados/microdados_enade_2010.csv',
                'enade_2011': 'microdados/microdados_enade_2011.csv',
                'enade_2012': 'microdados/microdados_enade_2012.csv'}
    ano = []
    regiao = []
    municipio = []
    idade = []
    sexo = []

    with open(arquivos['enade_2008']) as fp1:
        for linha in fp1.readlines()[1:]:
            nu_ano, co_ies, cd_catad, cd_orgac, co_grupo, co_subarea, co_regiao_habil, co_uf_habil, co_munic_habil, \
            co_curso, nu_idade, tp_sexo, sg_uf, ano_fim_2g, ano_in_gra, tp_semest, in_matut, in_vesper, in_noturno, \
            amostra, peso_amost, in_grad, in_inscr, tp_def_fis, tp_def_vis, tp_def_aud, tp_pres, tp_pr_ger, tp_pr_ob_fg, \
            tp_pr_di_fg, tp_pr_ob_ce, tp_pr_di_ce, tp_sfg_d1, tp_sfg_d2, tp_sce_d1, tp_sce_d2, tp_sce_d3, nu_que_ofg, \
            nu_que_dfg, nu_que_oce, nu_que_dce, vt_gab_ofg, vt_gab_oce, vt_esc_ofg, vt_ace_ofg, vt_esc_oce, vt_ace_oce, \
            nt_obj_fg, nt_fg_d1, nt_fg_d2, nt_dis_fg, nt_fg, nt_obj_ce, nt_ce_d1, nt_ce_d2, nt_ce_d3, nt_ce_d4, nt_ce_d5, \
            nt_ce_d6, nt_ce_d7, nt_ce_d8, nt_ce_d9, nt_ce_d10, nt_ce_d11, nt_ce_d12, nt_ce_d13, nt_ce_d14, nt_ce_d15, \
            nt_dis_ce, nt_ce, nt_ger, nu_que_qip, qp_i1, qp_i2, qp_i3, qp_i4, qp_i5, qp_i6, qp_i7, qp_i8, qp_i9, nu_que_soc, \
            tp_sit_soc, QE_I1, QE_I2, QE_I3, QE_I4, QE_I5, QE_I6, QE_I7, QE_I8, QE_I9, QE_I10, QE_I11, QE_I12, QE_I13, \
            QE_I14, QE_I15, QE_I16, QE_I17, QE_I18, QE_I19, QE_I20, QE_I21, QE_I22, QE_I23, QE_I24, QE_I25, QE_I26, QE_I27, \
            QE_I28, QE_I29, QE_I30, QE_I31, QE_I32, QE_I33, QE_I34, QE_I35, QE_I36, QE_I37, QE_I38, QE_I39, QE_I40, QE_I41, \
            QE_I42, QE_I43, QE_I44, QE_I45, QE_I46, QE_I47, QE_I48, QE_I49, QE_I50, QE_I51, QE_I52, QE_I53, QE_I54, QE_I55, \
            QE_I56, QE_I57, QE_I58, QE_I59, QE_I60, QE_I61, QE_I62, QE_I63, QE_I64, QE_I65, QE_I66, QE_I67, QE_I68, QE_I69, \
            QE_I70, QE_I71, QE_I72, QE_I73, QE_I74, QE_I75, QE_I76, QE_I77, QE_I78, QE_I79, QE_I80, QE_I81, QE_I82, QE_I83, \
            QE_I84, QE_I85, QE_I86, QE_I87, QE_I88, QE_I89, QE_I90, QE_I91, QE_I92, QE_I93, QE_I94, QE_I95, QE_I96, QE_I97, \
            QE_I98, QE_I99, QE_I100, QE_I101, QE_I102, QE_I103, QE_I104, QE_I105, QE_I106, QE_I107, QE_I108, QE_I109, \
            QE_I110, QE_I111, QE_I112, QE_I113, QE_I114, QE_I115 = linha.rstrip().split(';')
            ano.append(nu_ano)
            regiao.append(co_regiao_habil)
            municipio.append([sg_uf, co_munic_habil])
            idade.append(nu_idade)
            sexo.append(tp_sexo)


    with open(arquivos['enade_2009']) as fp2:
        for linha in fp2.readlines()[1:]:
            nu_ano, co_ies, cd_catad, cd_orgac, co_grupo, co_subarea, co_regiao_habil, co_uf_habil, co_munic_habil, \
            co_curso, nu_idade, tp_sexo, sg_uf, ano_fim_2g, ano_in_gra, tp_semest, in_matut, in_vesper, in_noturno, \
            amostra, peso_amost, in_grad, in_inscr, tp_def_fis, tp_def_vis, tp_def_aud, tp_pres, tp_pr_ger, tp_pr_ob_fg, \
            tp_pr_di_fg, tp_pr_ob_ce, tp_pr_di_ce, tp_sfg_d1, tp_sfg_d2, tp_sce_d1, tp_sce_d2, tp_sce_d3, nu_que_ofg, \
            nu_que_dfg, nu_que_oce, nu_que_dce, vt_gab_ofg, vt_gab_oce, vt_esc_ofg, vt_ace_ofg, vt_esc_oce, vt_ace_oce, \
            nt_obj_fg, nt_fg_d1, nt_fg_d2, nt_dis_fg, nt_fg, nt_obj_ce, nt_ce_d1, nt_ce_d2, nt_ce_d3, nt_ce_d4, nt_ce_d5, \
            nt_ce_d6, nt_ce_d7, nt_ce_d8, nt_ce_d9, nt_ce_d10, nt_ce_d11, nt_ce_d12, nt_ce_d13, nt_ce_d14, nt_ce_d15, \
            nt_dis_ce, nt_ce, nt_ger, nu_que_qip, qp_i1, qp_i2, qp_i3, qp_i4, qp_i5, qp_i6, qp_i7, qp_i8, qp_i9, nu_que_soc, \
            tp_sit_soc, QE_I1, QE_I2, QE_I3, QE_I4, QE_I5, QE_I6, QE_I7, QE_I8, QE_I9, QE_I10, QE_I11, QE_I12, QE_I13, \
            QE_I14, QE_I15, QE_I16, QE_I17, QE_I18, QE_I19, QE_I20, QE_I21, QE_I22, QE_I23, QE_I24, QE_I25, QE_I26, QE_I27, \
            QE_I28, QE_I29, QE_I30, QE_I31, QE_I32, QE_I33, QE_I34, QE_I35, QE_I36, QE_I37, QE_I38, QE_I39, QE_I40, QE_I41, \
            QE_I42, QE_I43, QE_I44, QE_I45, QE_I46, QE_I47, QE_I48, QE_I49, QE_I50, QE_I51, QE_I52, QE_I53, QE_I54, QE_I55, \
            QE_I56, QE_I57, QE_I58, QE_I59, QE_I60, QE_I61, QE_I62, QE_I63, QE_I64, QE_I65, QE_I66, QE_I67, QE_I68, QE_I69, \
            QE_I70, QE_I71, QE_I72, QE_I73, QE_I74, QE_I75, QE_I76, QE_I77, QE_I78, QE_I79, QE_I80, QE_I81, QE_I82, QE_I83, \
            QE_I84, QE_I85, QE_I86, QE_I87, QE_I88, QE_I89, QE_I90, QE_I91, QE_I92, QE_I93, QE_I94, QE_I95, QE_I96, QE_I97, \
            QE_I98, QE_I99, QE_I100, QE_I101, QE_I102, QE_I103, QE_I104, QE_I105, QE_I106, QE_I107, QE_I108, QE_I109, \
            QE_I110, QE_I111, QE_I112, QE_I113, QE_I114, QE_I115 = linha.rstrip().split(';')
            ano.append(nu_ano)
            regiao.append(co_regiao_habil)
            municipio.append([sg_uf, co_munic_habil])
            idade.append(nu_idade)
            sexo.append(tp_sexo)



    with open(arquivos['enade_2010']) as fp3:
        for linha in fp3.readlines()[1:]:
            nu_ano, co_ies, cd_catad, cd_orgac, co_grupo, co_subarea, co_regiao_habil, co_uf_habil, co_munic_habil, \
            co_curso, nu_idade, tp_sexo, sg_uf, ano_fim_2g, ano_in_gra, tp_semest, in_matut, in_vesper, in_noturno, \
            amostra, peso_amost, in_grad, in_inscr, tp_def_fis, tp_def_vis, tp_def_aud, tp_pres, tp_pr_ger, tp_pr_ob_fg, \
            tp_pr_di_fg, tp_pr_ob_ce, tp_pr_di_ce, tp_sfg_d1, tp_sfg_d2, tp_sce_d1, tp_sce_d2, tp_sce_d3, nu_que_ofg, \
            nu_que_dfg, nu_que_oce, nu_que_dce, vt_gab_ofg, vt_gab_oce, vt_esc_ofg, vt_ace_ofg, vt_esc_oce, vt_ace_oce, \
            nt_obj_fg, nt_fg_d1, nt_fg_d2, nt_dis_fg, nt_fg, nt_obj_ce, nt_ce_d1, nt_ce_d2, nt_ce_d3, nt_ce_d4, nt_ce_d5, \
            nt_ce_d6, nt_ce_d7, nt_ce_d8, nt_ce_d9, nt_ce_d10, nt_ce_d11, nt_ce_d12, nt_ce_d13, nt_ce_d14, nt_ce_d15, \
            nt_dis_ce, nt_ce, nt_ger, nu_que_qip, qp_i1, qp_i2, qp_i3, qp_i4, qp_i5, qp_i6, qp_i7, qp_i8, qp_i9, nu_que_soc, \
            tp_sit_soc, QE_I1, QE_I2, QE_I3, QE_I4, QE_I5, QE_I6, QE_I7, QE_I8, QE_I9, QE_I10, QE_I11, QE_I12, QE_I13, \
            QE_I14, QE_I15, QE_I16, QE_I17, QE_I18, QE_I19, QE_I20, QE_I21, QE_I22, QE_I23, QE_I24, QE_I25, QE_I26, QE_I27, \
            QE_I28, QE_I29, QE_I30, QE_I31, QE_I32, QE_I33, QE_I34, QE_I35, QE_I36, QE_I37, QE_I38, QE_I39, QE_I40, QE_I41, \
            QE_I42, QE_I43, QE_I44, QE_I45, QE_I46, QE_I47, QE_I48, QE_I49, QE_I50, QE_I51, QE_I52, QE_I53, QE_I54, QE_I55, \
            QE_I56, QE_I57, QE_I58, QE_I59, QE_I60, QE_I61, QE_I62, QE_I63, QE_I64, QE_I65, QE_I66, QE_I67, QE_I68, QE_I69, \
            QE_I70, QE_I71, QE_I72, QE_I73, QE_I74, QE_I75, QE_I76, QE_I77, QE_I78, QE_I79, QE_I80, QE_I81, QE_I82, QE_I83, \
            QE_I84, QE_I85, QE_I86, QE_I87, QE_I88, QE_I89, QE_I90, QE_I91, QE_I92, QE_I93, QE_I94, QE_I95, QE_I96, QE_I97, \
            QE_I98, QE_I99, QE_I100, QE_I101, QE_I102, QE_I103, QE_I104, QE_I105, QE_I106, QE_I107, QE_I108, QE_I109, \
            QE_I110, QE_I111, QE_I112, QE_I113, QE_I114, QE_I115 = linha.rstrip().split(';')
            ano.append(nu_ano)
            regiao.append(co_regiao_habil)
            municipio.append([sg_uf, co_munic_habil])
            idade.append(nu_idade)
            sexo.append(tp_sexo)


    with open(arquivos['enade_2011']) as fp4:
        for linha in fp4.readlines()[1:]:
            nu_ano, co_ies, cd_catad, cd_orgac, co_grupo, co_subarea, co_regiao_habil, co_uf_habil, co_munic_habil, \
            co_curso, nu_idade, tp_sexo, sg_uf, ano_fim_2g, ano_in_gra, tp_semest, in_matut, in_vesper, in_noturno, \
            amostra, peso_amost, in_grad, in_inscr, tp_def_fis, tp_def_vis, tp_def_aud, tp_pres, tp_pr_ger, tp_pr_ob_fg, \
            tp_pr_di_fg, tp_pr_ob_ce, tp_pr_di_ce, tp_sfg_d1, tp_sfg_d2, tp_sce_d1, tp_sce_d2, tp_sce_d3, nu_que_ofg, \
            nu_que_dfg, nu_que_oce, nu_que_dce, vt_gab_ofg, vt_gab_oce, vt_esc_ofg, vt_ace_ofg, vt_esc_oce, vt_ace_oce, \
            nt_obj_fg, nt_fg_d1, nt_fg_d2, nt_dis_fg, nt_fg, nt_obj_ce, nt_ce_d1, nt_ce_d2, nt_ce_d3, nt_ce_d4, nt_ce_d5, \
            nt_ce_d6, nt_ce_d7, nt_ce_d8, nt_ce_d9, nt_ce_d10, nt_ce_d11, nt_ce_d12, nt_ce_d13, nt_ce_d14, nt_ce_d15, \
            nt_dis_ce, nt_ce, nt_ger, nu_que_qip, qp_i1, qp_i2, qp_i3, qp_i4, qp_i5, qp_i6, qp_i7, qp_i8, qp_i9, nu_que_soc, \
            tp_sit_soc, QE_I1, QE_I2, QE_I3, QE_I4, QE_I5, QE_I6, QE_I7, QE_I8, QE_I9, QE_I10, QE_I11, QE_I12, QE_I13, \
            QE_I14, QE_I15, QE_I16, QE_I17, QE_I18, QE_I19, QE_I20, QE_I21, QE_I22, QE_I23, QE_I24, QE_I25, QE_I26, QE_I27, \
            QE_I28, QE_I29, QE_I30, QE_I31, QE_I32, QE_I33, QE_I34, QE_I35, QE_I36, QE_I37, QE_I38, QE_I39, QE_I40, QE_I41, \
            QE_I42, QE_I43, QE_I44, QE_I45, QE_I46, QE_I47, QE_I48, QE_I49, QE_I50, QE_I51, QE_I52, QE_I53, QE_I54, QE_I55, \
            QE_I56, QE_I57, QE_I58, QE_I59, QE_I60, QE_I61, QE_I62, QE_I63, QE_I64, QE_I65, QE_I66, QE_I67, QE_I68, QE_I69, \
            QE_I70, QE_I71, QE_I72, QE_I73, QE_I74, QE_I75, QE_I76, QE_I77, QE_I78, QE_I79, QE_I80, QE_I81, QE_I82, QE_I83, \
            QE_I84, QE_I85, QE_I86, QE_I87, QE_I88, QE_I89, QE_I90, QE_I91, QE_I92, QE_I93, QE_I94, QE_I95, QE_I96, QE_I97, \
            QE_I98, QE_I99, QE_I100, QE_I101, QE_I102, QE_I103, QE_I104, QE_I105, QE_I106, QE_I107, QE_I108, QE_I109, \
            QE_I110, QE_I111, QE_I112, QE_I113, QE_I114, QE_I115 = linha.rstrip().split(';')
            ano.append(nu_ano)
            regiao.append(co_regiao_habil)
            municipio.append([sg_uf, co_munic_habil])
            idade.append(nu_idade)
            sexo.append(tp_sexo)



    with open(arquivos['enade_2012']) as fp5:
        for linha in fp5.readlines()[1:]:
            nu_ano, co_ies, cd_catad, cd_orgac, co_grupo, co_subarea, co_regiao_habil, co_uf_habil, co_munic_habil, \
            co_curso, nu_idade, tp_sexo, sg_uf, ano_fim_2g, ano_in_gra, tp_semest, in_matut, in_vesper, in_noturno, \
            amostra, peso_amost, in_grad, in_inscr, tp_def_fis, tp_def_vis, tp_def_aud, tp_pres, tp_pr_ger, tp_pr_ob_fg, \
            tp_pr_di_fg, tp_pr_ob_ce, tp_pr_di_ce, tp_sfg_d1, tp_sfg_d2, tp_sce_d1, tp_sce_d2, tp_sce_d3, nu_que_ofg, \
            nu_que_dfg, nu_que_oce, nu_que_dce, vt_gab_ofg, vt_gab_oce, vt_esc_ofg, vt_ace_ofg, vt_esc_oce, vt_ace_oce, \
            nt_obj_fg, nt_fg_d1, nt_fg_d2, nt_dis_fg, nt_fg, nt_obj_ce, nt_ce_d1, nt_ce_d2, nt_ce_d3, nt_ce_d4, nt_ce_d5, \
            nt_ce_d6, nt_ce_d7, nt_ce_d8, nt_ce_d9, nt_ce_d10, nt_ce_d11, nt_ce_d12, nt_ce_d13, nt_ce_d14, nt_ce_d15, \
            nt_dis_ce, nt_ce, nt_ger, nu_que_qip, qp_i1, qp_i2, qp_i3, qp_i4, qp_i5, qp_i6, qp_i7, qp_i8, qp_i9, nu_que_soc, \
            tp_sit_soc, QE_I1, QE_I2, QE_I3, QE_I4, QE_I5, QE_I6, QE_I7, QE_I8, QE_I9, QE_I10, QE_I11, QE_I12, QE_I13, \
            QE_I14, QE_I15, QE_I16, QE_I17, QE_I18, QE_I19, QE_I20, QE_I21, QE_I22, QE_I23, QE_I24, QE_I25, QE_I26, QE_I27, \
            QE_I28, QE_I29, QE_I30, QE_I31, QE_I32, QE_I33, QE_I34, QE_I35, QE_I36, QE_I37, QE_I38, QE_I39, QE_I40, QE_I41, \
            QE_I42, QE_I43, QE_I44, QE_I45, QE_I46, QE_I47, QE_I48, QE_I49, QE_I50, QE_I51, QE_I52, QE_I53, QE_I54, QE_I55, \
            QE_I56, QE_I57, QE_I58, QE_I59, QE_I60, QE_I61, QE_I62, QE_I63, QE_I64, QE_I65, QE_I66, QE_I67, QE_I68, QE_I69, \
            QE_I70, QE_I71, QE_I72, QE_I73, QE_I74, QE_I75, QE_I76, QE_I77, QE_I78, QE_I79, QE_I80, QE_I81, QE_I82, QE_I83, \
            QE_I84, QE_I85, QE_I86, QE_I87, QE_I88, QE_I89, QE_I90, QE_I91, QE_I92, QE_I93, QE_I94, QE_I95, QE_I96, QE_I97, \
            QE_I98, QE_I99, QE_I100, QE_I101, QE_I102, QE_I103, QE_I104, QE_I105, QE_I106, QE_I107, QE_I108, QE_I109, \
            QE_I110, QE_I111, QE_I112, QE_I113, QE_I114, QE_I115 = linha.rstrip().split(';')
            ano.append(nu_ano)
            regiao.append(co_regiao_habil)
            municipio.append([sg_uf, co_munic_habil])
            idade.append(nu_idade)
            sexo.append(tp_sexo)





    return dict_info