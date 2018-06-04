import FWCore.ParameterSet.Config as cms

process = cms.Process('HLTANALYZER')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:skim_Run2017D_SingleElectron.root'), # skimmed file on EOS at LPC
    #fileNames = cms.untracked.vstring('/store/data/Run2017D/SingleElectron/MINIAOD/31Mar2018-v1/100000/06300247-1239-E811-A8C5-A4BF01027688.root'), # skimmed file on EOS at LPC
)


process.options = cms.untracked.PSet(

)

#import FWCore.PythonUtilities.LumiList as LumiList
#process.source.lumisToProcess = LumiList.LumiList(filename = 'Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt').getVLuminosityBlockRange()


# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.20 $'),
    annotation = cms.untracked.string('RelVal nevts:100'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.TFileService = cms.Service("TFileService",
                                       fileName = cms.string('histos_METTrigAnalyzer.root')
                                   )

### analyzer configuration

process.metTrigAnalyzerMiniAOD = cms.EDAnalyzer("METTrigAnalyzerMiniAOD")
process.metTrigAnalyzerMiniAOD.refTriggerName = cms.untracked.string("HLT_Ele27_WPTight_Gsf_v14")
process.metTrigAnalyzerMiniAOD.sigTriggerName = cms.untracked.string("HLT_PFMET200_HBHECleaned_v5")
process.metTrigAnalyzerMiniAOD.verbose = cms.untracked.bool(False)

process.GlobalTag.globaltag = "94X_dataRun2_ReReco_EOY17_v6"

# Path and EndPath definitions
process.HLTanalyzers = cms.Path(process.metTrigAnalyzerMiniAOD)
